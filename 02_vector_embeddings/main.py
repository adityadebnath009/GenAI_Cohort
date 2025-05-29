# from openai import OpenAI
import os
import pprint
import json


from dotenv import load_dotenv
load_dotenv()
# Get the API key from environment
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the OpenAI client
# client = OpenAI(api_key=api_key,
#                 base_url = "https://generativelanguage.googleapis.com/v1beta/openai/")




# text = "Dog chases cat."
# # Get the embeddings for the text
# response = client.embeddings.create(
#     model = "gemini-2.0-flash",
#     input = text
# )

# print(response)

# from google import genai

# client = genai.Client(api_key="GEMINI_API_KEY")

# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents=["How does AI work?"]
# )
# print(response.text)


from openai import OpenAI

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Hi"
        }
    ]
)
print(type(response))#<class 'openai.types.chat.chat_completion.ChatCompletion'> Response is a object of ChatCompletions
# pprint.pprint(response)

print(json.dumps(response.model_dump(), indent=2))

print(response.choices[0].message.content)