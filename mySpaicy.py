import os
from dotenv import load_dotenv

import openai
import spacy

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

usedModel = "gpt-3.5-turbo-instruct"
prompt = 'Cuentame una historia breve sobre un viaje a Colombia'

responseAI = openai.Completion.create(
    engine=usedModel,
    prompt=prompt,
    # number of responses
    n=1,
    # level of creativity 0.1 to 1 (More creative)
    #  temperature=1,
    # number of characters in response
    max_tokens=100
)

responseFormat = responseAI.choices[0].text.strip()
print(responseFormat)
print('****')

usedModel = spacy.load("es_core_news_md")
spacyResponse = usedModel(responseFormat)
for token in spacyResponse:
    print(token.text, token.pos_, token.head.text)
print('****')
for ent in spacyResponse.ents:
    print(ent.text, ent.label_)

print('****')
newLocation = None
for ent in spacyResponse.ents:
    if ent.label_ == 'LOC':
        newLocation = ent

if newLocation:
    prompt2 = f"Dame mas informacion sobre {newLocation}"
    usedModel = "gpt-3.5-turbo-instruct"
    response2 = openai.Completion.create(
        engine=usedModel,
        prompt=prompt2,
        # number of responses
        n=1,
        # level of creativity 0.1 to 1 (More creative)
        #  temperature=1,
        # number of characters in response
        max_tokens=100
    )
    print(response2.choices[0].text.strip())
    print('****')
else:
    print('No location')
