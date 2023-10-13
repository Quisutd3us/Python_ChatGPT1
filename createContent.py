import os
from dotenv import load_dotenv

import openai

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

