from pydantic import BaseModel
from typing import Optional
from openai import OpenAI

def process_job_posting(unstructured_text):
    """
    Processes unstructured job posting text and returns structured data.
    This function integrates with GPT-4 API to extract information.
    """
    # Define the structured data model
    class JobPosting(BaseModel):
        job_title: Optional[str]
        company_name: Optional[str]
        location: Optional[str]
        job_description: Optional[str]
        requirements: Optional[str]
        benefits: Optional[str]
        application_deadline: Optional[str]
        contact_information: Optional[str]

    # Create the OpenAI client
    client = OpenAI()

    # Construct the messages
    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert at structured data extraction. "
                "You will be given unstructured text from a job posting "
                "and should convert it into the given structure."
            ),
        },
        {"role": "user", "content": unstructured_text},
    ]

    # Call the OpenAI API using the parse method
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=messages,
        response_format=JobPosting,
    )

    # Extract the parsed data
    job_posting = completion.choices[0].message.parsed

    # Return the structured data as a dictionary
    return job_posting.dict()
