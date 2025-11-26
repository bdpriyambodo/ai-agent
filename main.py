import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main(user_prompt=None, flag_prompt=None): 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
    )

    print(response.text)

    if flag_prompt == '--verbose':
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count }")


if len(sys.argv) < 2:
    print("Usage: python3 main.py 'prompt'")
    sys.exit(1)
elif len(sys.argv) == 2:
    user_prompt = sys.argv[1]
    main(user_prompt)    
elif len(sys.argv) == 3:
    if sys.argv[1].startswith('--'):
        flag_prompt = sys.argv[1]
        user_prompt = sys.argv[2]
        main(user_prompt, flag_prompt)
    elif sys.argv[2].startswith('--'):
        flag_prompt = sys.argv[2]
        user_prompt = sys.argv[1]
        main(user_prompt, flag_prompt)




# def main():
#     print("Hello from ai-agent!")


# if __name__ == "__main__":
#     main()
