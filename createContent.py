import os
from dotenv import load_dotenv

import openai

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


# Define functions
def create_content(fn_engine, subject, fn_n, fn_temperature, fn_max_tokens):
    fn_prompt = f"Please write a complete article in English about this subject :{subject}"
    response_ai = openai.Completion.create(
        engine=fn_engine,
        prompt=fn_prompt,
        n=fn_n,
        temperature=fn_temperature,
        max_tokens=fn_max_tokens
    )
    return response_ai.choices[0].text.strip()


def create_resume(fn_engine, fn_content, fn_n, fn_temperature, fn_max_tokens):
    fn_prompt = f"Create a compressible resume this text in English : {fn_content}"
    response_ai = openai.Completion.create(
        engine=fn_engine,
        prompt=fn_prompt,
        n=fn_n,
        temperature=fn_temperature,
        max_tokens=fn_max_tokens
    )
    return response_ai.choices[0].text.strip()


# Call Functions

content_ai = create_content("gpt-3.5-turbo-instruct",
                            'Fentanyl',
                            1,
                            1.5,
                            500)

print(f"{content_ai}")
print('--------------------')

print(f"{create_resume('gpt-3.5-turbo-instruct', content_ai, 1, 1.5, 100)}")
