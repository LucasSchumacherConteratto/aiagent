import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
import prompts

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():

    if api_key is None:
        raise RuntimeError("API KEY NOT FOUND")    
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="Description to be sent to Gemini.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    gemini_response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages,
        config=types.GenerateContentConfig(system_instruction=prompts.system_prompt,temperature=0)
    )
    
    if gemini_response is None:
        raise RuntimeError("Error receiving response from Gemini!")
    
    if args.verbose is True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {gemini_response.usage_metadata.prompt_token_count}\nResponse tokens: {gemini_response.usage_metadata.candidates_token_count}\n")

    
    print(gemini_response.text)

if __name__ == "__main__":
    main()
