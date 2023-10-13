import os
from dotenv import load_dotenv
import numpy as np
import openai

# upload .txt file
filename = 'histories.txt'
data = np.loadtxt(filename, delimiter='~', dtype=str)

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


# Define Functions

def do_analyze_feelings(fn_engine, fn_text, fn_n, fn_temperature, fn_max_tokens):
    fn_prompt = f"Please analyze the prevailing sentiment in the following text  :{fn_text}"
    response_ai = openai.Completion.create(
        engine=fn_engine,
        prompt=fn_prompt,
        n=fn_n,
        temperature=fn_temperature,
        max_tokens=fn_max_tokens
    )
    return response_ai.choices[0].text.strip()


print(f"{do_analyze_feelings('gpt-3.5-turbo-instruct', data, 1, 1.5, 500)}")
