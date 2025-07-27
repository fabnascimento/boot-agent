import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    validate_arguments()
    user_prompt = get_user_prompt()

    messages = [
        types.Content(role="user", parts=[
            types.Part(text=user_prompt)
        ])
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    print(response.text)

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    os._exit(0)


def validate_arguments():
    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt>")
        os._exit(1)

def get_user_prompt():
    return sys.argv[1]

if __name__ == "__main__":
    main()
