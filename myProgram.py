import os
from dotenv import load_dotenv

import openai

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

usedModel = "gpt-3.5-turbo-instruct"
prompt = 'give me a poem about python program language'

responseAI = openai.Completion.create(
    engine=usedModel,
    prompt=prompt,
    # number of responses
    n=3,
    # level of creativity 0.1 to 1 (More creative)
    temperature=1,
    # number of characters in response
    max_tokens=50
)

for idx, option in enumerate(responseAI.choices):
    formatResponse = option.text.strip()
    print(f"Response {idx + 1}: {formatResponse}\n")
    print('---------------------------------------')
