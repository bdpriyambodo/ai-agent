import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
from call_function import (
    schema_get_files_info, 
    available_functions,
    call_function
)

def check_all_candidates_function_call(candidate):
    for part in candidate.content.parts:
        if hasattr(part, "function_call") and part.function_call is not None:
            return True
    return False    

def main(user_prompt=None, flag_prompt=None): 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    iteration = 1
    flag_function_call_candidate = True
    flag_response_text = True

    messages = []

    while iteration <= 20 and flag_function_call_candidate and flag_response_text:

        messages.append(
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        )

        response = client.models.generate_content(
            model='gemini-2.0-flash-001', contents=messages,
            config= types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt)
        )

        # list all candidate property from response:
        for i, candidate in enumerate(response.candidates): 
            messages.append(candidate.content)

        flag_function_call_candidate = all(
            check_all_candidates_function_call(candidate) for candidate in response.candidates
        )

        # flag_function_call_candidate = not all(c.function_call is None for c in response.candidates)
        if not flag_function_call_candidate:
            if response.text and response.text.strip():
                flag_response_text = True

        temp_list = []

        if response.function_calls is None:
            print(response.text)
        else:
            for i in response.function_calls:
                # print(f"Calling function: {i.name}({i.args})")

                function_call_result = call_function(
                    i.name,
                    **i.args
                    )

                if function_call_result.parts[0].function_response.response is None:
                    raise Exception('No response')
                else:
                    temp_list.append(function_call_result.parts[0])

                # if function_call_result.parts[0].function_response.response:
                #     temp_list.append(function_call_result.parts[0])
                # else:
                #     raise Exception('No response')

    if flag_prompt == '--verbose':
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count }")
        print(f"-> {function_call_result.parts[0].function_response.response}")   

    print(f"Iteration: {iteration}")

 
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
