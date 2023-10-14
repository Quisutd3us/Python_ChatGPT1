import os
from dotenv import load_dotenv
import openai
import spacy

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

model_spacy = spacy.load("es_core_news_md")
black_list = ["sex", "nudes"]

history_answers = []
history_questions = []


def filter_black_list(fn_response_ai, fn_black_list):
    token = model_spacy(fn_response_ai)
    filter_result = []
    for t in token:
        if t.text.lower() not in fn_black_list:
            filter_result.append(t.text)
        else:
            filter_result.append("['PROHIBITED-WORD']")
    return " ".join(filter_result)


def ask_chat_gpt(fn_prompt, model="gpt-3.5-turbo-instruct"):
    response_ai = openai.Completion.create(
        engine=model,
        prompt=fn_prompt,
        # number of responses
        n=1,
        # level of creativity 0.1 to 1 (More creative)
        temperature=0.1,
        # number of characters in response
        max_tokens=150
    )
    return filter_black_list(response_ai.choices[0].text.strip(), black_list)


print('Welcome to Our ChatBot, Write EXIT when you will Finish...')

while True:
    format_history_conversation = ""
    for question, response in zip(history_questions, history_answers):
        format_history_conversation += f"The User ask: {question}\n"
        format_history_conversation += f"ChatBot answer: {response}\n"
    user_input = input('\nYou:')
    if user_input.lower() == 'exit':
        break
    prompt = f"The user Ask: {user_input}\n"
    format_history_conversation += prompt
    response = ask_chat_gpt(format_history_conversation)
    print(f"{response}")

    history_questions.append(user_input)
    history_answers.append(response)
