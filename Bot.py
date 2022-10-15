import os
from unittest.util import _MAX_LENGTH
import openai
import streamlit as st
openai.api_key = os.getenv('OPENAI_API_KEY')


start_sequence = "\nAI:"
restart_sequence = "\n\Humano:"

text_example = read_text_example()
session_prompt = "Lo que sigue es una conversación con un asistente de AI. El asistente es un experto en vinos, servicial, creativo, inteligente y muy amable. Si no sabe la respuesta a algun pregunta, responde: 'No puedo responder esa pregunta por ahora. Trate de nuevo más tarde, por favor'"+text_example+data 
def mises(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        temperature=0.7,
        # max_length=250,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def read_text_example():
    f = open('texto.txt', 'r')
    content = f.read()
    print(content)
    return content

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
