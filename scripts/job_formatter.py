import json
import sys
from openai import OpenAI

def load_schema(schema_file):
    """Loads the JSON schema from a file."""
    with open(schema_file, 'r') as file:
        return json.load(file)

def main():
    # Load the schema from a separate file
    schema_file = "/home/guinn8/Documents/resume/scripts/job_schema.json"
    json_schema = load_schema(schema_file)

   # Check if data is being piped into the script
    if not sys.stdin.isatty():
        # Read piped input
        prompt = sys.stdin.read().strip()
    else:
        print("No prompt")
        exit(0)


    print(f"Formatting the following posting:\n\n {prompt}")

    # Initialize OpenAI client
    client = OpenAI()

    # Print the response
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a job posting formatter. You are tasked with converting the inputted job posting and producing a json object. The output json should be a verbatim copy all details from the input."},
                {"role": "user", "content": prompt}
            ],
            metadata={
                "tag": "job_posting",
            },
            temperature=1,
            max_tokens=2048,
            top_p=1,
            store=True,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={
                "type": "json_schema",
                "json_schema": json_schema
            }
        )

        # Pretty print the response
        import pprint
        pprint.pprint(json.loads(response.choices[0].message.content))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
