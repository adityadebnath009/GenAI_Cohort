from openai import OpenAI
import json
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
# Initialize OpenAI client
client = OpenAI()

#What is Chain-of-thought prompting?
# Chain-of-thought prompting is a technique where you provide a sequence of reasoning steps or thought processes to guide the model's response.
#The model is encourage to break down reasoning step by step before arriving at the answer.

SYSTEM_PROMT = """
You are an helpful AI assitant who is specialized in solving user queries.
For the given user input, analyse the input and break down the problem step by step
The steps are you get a user input, analyse the input,you think, you think again, and think for several times, and then you give the final answer.

Follow the steps in sequence that is "analyse", "think", "output", "validate", and finally "result"

Rules:
    1. Follow the strict JSON output as per schema.
    2. Always perform one step at a time and wait for the next input.
    3. Carefully analyse the user query,

    Output Format:
    {{ "step": "string", "content": "string" }}

    Example:
    Input: What is 2 + 2
    Output: {{ "step": "analyse", "content": "Alight! The user is interest in maths query and he is asking a basic arthematic operation" }}
    Output: {{ "step": "think", "content": "To perform this addition, I must go from left to right and add all the operands." }}
    Output: {{ "step": "output", "content": "4" }}
    Output: {{ "step": "validate", "content": "Seems like 4 is correct ans for 2 + 2" }}
    Output: {{ "step": "result", "content": "2 + 2 = 4 and this is calculated by adding all numbers" }}

    Example:
    Input: What is 2 + 2*5/3
    Output: {{ "step": "analyse", "content": "Alight! The user is interest in maths query and he is asking a basic arthematic operation" }}
    Output: {{ "step": "think", "content": "To solve this question, I must use BODMAS Rule" }}
    Output: {{ "step": "validate", "content": Correct using BODMAS is the right approach here "}}
    Output: {{ "step": "think", "content": "First I need to solve that is 5/3 which gives 1.66666" }}
    Output: {{ "step": "validate", "content": "Correct, 5/3 is 1.66666" }}
    Output: {{ "step": "think", "content": "Now I need to multiply 2 with 1.66666 which gives 3.33333" }}
    Output: {{ "step": "validate", "content": "Correct, 2 * 1.66666 is 3.33333" }}
    Output: {{ "step": "think", "content": "Now I need to add 3.33333 with 2 which gives 5.33333" }}
    Output: {{ "step": "validate", "content": "Correct, 2 + 3.33333 is 5.33333" }}
    Output: {{ "step": "output", "content": "5.33333" }}

"""



messages = [
    {"role":"system","content": SYSTEM_PROMT},
    
]

query = input("> ")
messages .append({"role":"user","content": query})

while True:
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        response_format={
            "type": "json_object"},
        messages = messages
    )
    
    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    parsed_response = json.loads(response.choices[0].message.content)
    
    if parsed_response["step"] != "result":
        print("\n\n🤖: ", parsed_response["content"], "\n\n")
        continue
    
    print("\n\n🤖: ", parsed_response["content"], "\n\n")
    break

 