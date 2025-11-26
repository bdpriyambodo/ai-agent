import sys
import os
from dotenv import load_dotenv
from google import genai

def main(prompt_input): 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=prompt_input
    )
    print(response.text)

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count }")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])


# def main():
#     print("Hello from ai-agent!")


# if __name__ == "__main__":
#     main()
