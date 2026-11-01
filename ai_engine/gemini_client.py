
import os
import logging

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

DEFAULT_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-20b"
)

client = None


def get_client():
    global client

    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY is missing from your .env file."
        )

    if client is None:
        client = OpenAI(
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1",
            timeout=60.0,
            max_retries=1
        )

    return client


def generate_response(
    prompt,
    model_name=None,
    system_prompt=None,
    **kwargs
):

    if not prompt or not str(prompt).strip():
        raise ValueError("Prompt cannot be empty.")

    selected_model = model_name or DEFAULT_MODEL

    api_client = get_client()

    messages = []

    # Add system instructions separately
    if system_prompt and system_prompt.strip():
        messages.append({
            "role": "system",
            "content": system_prompt.strip()
        })

    # Add user's actual question
    messages.append({
        "role": "user",
        "content": str(prompt)
    })

    logger.info(
        "Sending request to Groq: %s",
        selected_model
    )

    response = api_client.chat.completions.create(
        model=selected_model,
        messages=messages,
        max_completion_tokens=8192,
        reasoning_effort="low",
        temperature=0.2
    )

    message = response.choices[0].message
    answer = message.content

    if not answer or not answer.strip():

        logger.error(
            "Empty response. Finish reason: %s",
            response.choices[0].finish_reason
        )

        raise ValueError(
            "Groq returned an empty response."
        )

    logger.info(
        "Groq response received successfully."
    )

    return answer.strip()
