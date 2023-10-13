import os
from dotenv import load_dotenv
import openai

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

history_answers = []
history_questions = []


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
    return response_ai.choices[0].text.strip()


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
