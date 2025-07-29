import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


def main():
    api_key = get_api_key()
    client = genai.Client(api_key=api_key)

    args = retrieve_arguments()

    messages = [
        types.Content(role="user", parts=[
            types.Part(text=args.prompt),
        ])
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    print(response.text)

    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    sys.exit(0)


def get_api_key():
    if not os.environ.get("GEMINI_API_KEY"):
        print("API Key not provided")
        sys.exit(1)

    return os.environ.get("GEMINI_API_KEY")

def validate_arguments():
    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt>")
        sys.exit(1)

def get_user_prompt():
    return sys.argv[1]


def retrieve_arguments():
    validate_arguments()

    parser = argparse.ArgumentParser()
    # positional argument
    parser.add_argument("prompt")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose print with some statistics")

    return parser.parse_args()


if __name__ == "__main__":
    main()
