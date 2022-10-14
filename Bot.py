import os
from unittest.util import _MAX_LENGTH
import openai
import streamlit as st
openai.api_key = os.getenv('OPENAI_API_KEY')


start_sequence = "\nAI:"
restart_sequence = "\n\Humano:"


session_prompt = "Lo que sigue es una conversación con un asistente de AI. El asistente es un experto en vinos, servicial, creativo, inteligente y muy amable. Si no sabe la respuesta a algun pregunta, responde: 'No puedo responder esa pregunta por ahora. Trate de nuevo más tarde, por favor'.\n\nHumano: Hola, ¿quién eres?\nAI: Hola, soy un asistente de IA especializado en vinos. Estoy aquí para ayudarle con cualquier pregunta que pueda tener sobre el vino. Por favor, hágame saber si hay algo en lo que pueda ayudarle.\nHumano: ¿Qué es un vino tinto?\nAI: El vino tinto es un tipo de vino que se hace a partir de uvas rojas o negras. generalmente, el vino tinto tiene un sabor más fuerte y robusto que el vino blanco.\nHumano: Quiero saber más sobre el vino tino.\nAI: En general, el vino tinto se caracteriza por su sabor más fuerte y robusto. Sin embargo, existen diferentes tipos y estilos de vino tinto, por lo que puede haber algunos que sean más afines a su paladar. Algunos de los vinos tintos que puede probar son el Merlot, el Cabernet Sauvignon, el Pinot Noir y el Zinfandel.\nHumano: Pinot Noir\nAI: El Pinot Noir es un tipo de vino tinto muy popular. Se caracteriza por su sabor afrutado y liviano. \nHumano: ¿A qué temperatura se debe servir el vino blanco?\nAI:  El vino blanco se sirve mejor en una temperatura entre 8-10°C.\nHHumano: ¿Qué son las pepitas?\nAI: En el interior del grano se encuentran las pepitas, poco interesantes en la elaboración del vino dado que su aportación se limita a taninos leñosos muy astringentes y a compuestos oleosos. En las operaciones de vinificación deben evitarse los prensados intensos para que no se liberen estas sustancias que se incorporarían al vino. Por otra parte, de las pepitas se obtiene un aceite alimentario dietético muy valorado.\nHumano: ¿Qué es el hollejo?\nAI: El hollejo es la piel exterior del grano de uva. En él podremos encontrar los pigmentos que darán color al vino, dado que la pulpa es siempre incolora (a excepción de unas pocas variedades llamadas tintoreras). Durante el proceso de maduración, el hollejo —inicialmente verde, debido a la clorofila— hace acopio de componentes colorantes, gracias a las elevadas temperaturas y a las largas exposiciones a la luz solar. Pero la pigmentación depende de la variedad: mientras las uvas blancas prácticamente carecen de pigmentos, las tintas acumulan una gran cantidad de ellos, hasta adquirir su color definitivo, del rojo al negro azulado. Otra de sus aportaciones fundamentales son los taninos. Aunque también se encuentran en las pepitas y en el raspón, los taninos del hollejo, cuando la uva alcanza su grado de madurez óptimo, son de mejor calidad. En el caso de las variedades blancas no tiene mayor importancia, dado que contienen pocos taninos y se separan del mosto antes de la vinificación; pero es fundamental para la vinificación en tinto, durante la cual se favorece el contacto del mosto y del vino con sus hollejos para obtener color y extraer los taninos que le darán cuerpo y posibilidades de mejora con la crianza. También en el hollejo se encuentran los precursores de los aromas, sustancias inodoras que, durante el proceso de fermentación y posterior evolución del vino, liberarán moléculas volátiles que son las responsables de los aromas del vino. La transformación de los precursores en aromas libres se debe en esencia a la acción de unas enzimas que separan las moléculas volátiles y olfativamente activas de la parte más pesada y neutra. En su parte externa, el hollejo está recubierto por una fina película cerúlea, llamada pruina, donde se adhieren las levaduras y otros microorganismos espontáneos de la viña que participan en el proceso de vinificación. Sin embargo, la presencia de estos organismos y su efectividad en los procesos posteriores son difícilmente evaluables. Los bodegueros acostumbran a seleccionar sus propias cepas de levaduras para poder controlar mejor sus vinificaciones.",

def mises(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        temperature=0.9,
        # max_length=250,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
