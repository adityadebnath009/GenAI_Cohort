from openai import OpenAI
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
# Initialize OpenAI client
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
#One-shot prompting example 
#What is one-shot prompting?
# One-shot prompting is a technique where you provide a single example of the desired input-output pair to guide the model's response.
# It helps the model understand the context and format of the response you expect, allowing it to generate more relevant and accurate outputs.
# In this example, we will create a system prompt that instructs the model to respond only to Python-related queries and roast the user for non-Python questions.
SYSTEM_PROMT = """
You are an AI expert in Coding. You only know Python and nothing else.
You only help users in solving their python doubts only and nothing else.
If the user tried to ask you anything other than python, you can roast him.
"""

response = client.chat.completions.create(
    model = "gemini-2.0-flash",
    messages = [
        {"role":"system", "content": SYSTEM_PROMT},
        {"role":"user","content":"Hey, My name is Aditya"},
        {"role":"assistant","content":"Hello Aditya, If you have any python related queries, feel free to ask."},
        {"role":"user","content":"How I can Make a chai?"},
        {"role":"assistant","content":"I am not a chef, I am a python expert. Ask me python related queries."},
        {"role":"user","content":"How to write a code in python to add two numbers?"}
    ]
)

print(response.choices[0].message.content)