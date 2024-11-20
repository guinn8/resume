import json
import sys
import subprocess
from openai import OpenAI


def load_schema(schema_file):
    """Loads the JSON schema from a file."""
    with open(schema_file, 'r') as file:
        return json.load(file)


def get_git_hash():
    """Retrieves the short Git hash of the current repository state."""
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode().strip()
    except Exception:
        return "unknown"


def main():
    # Load the schema from a separate file
    schema_file = "/home/guinn8/Documents/resume/scripts/job_schema.json"
    json_schema = load_schema(schema_file)

    if not sys.stdin.isatty():
        prompt = sys.stdin.read().strip()
    else:
        print("No prompt")
        exit(0)

    print(f"Formatting the following posting:\n\n {prompt}")
    client = OpenAI()

    git_hash = get_git_hash()  # Retrieve the short Git hash

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a job posting formatter."
                                              "You are tasked with converting the inputted job posting and producing a json object."
                                              "The output json should carefully copy all, EACH AND EVERY detail from the input job posting."
                                              "You will be evaluated on how well you reproduce all the relevant data from the job posting in the final json."},
                {"role": "user", "content": prompt}
            ],
            metadata={
                "tag": "job_posting",
                "git_hash": git_hash  # Include the Git hash
            },
            temperature=0.2,
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

        import pprint
        pprint.pprint(json.loads(response.choices[0].message.content))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
