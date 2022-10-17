import os
from unittest.util import _MAX_LENGTH
import nlpcloud
import streamlit as st
nlpcloud.api_key = os.getenv('TOKEN')


start_sequence = "\nAI:"
restart_sequence = "\n\Humano:"

def client = nlpcloud.Client("<model_name>", "<token>", gpu=True)
    client.generation("Dados los siguientes valores, haga una seccion de pruntas frecuentes,\n\nEN QUÉ CREEMOS, VALORES Y VIRTUDES\n\nInstituto Fe y Libertad\nReescritura 2022\nEN QUÉ CREEMOS (postulados, principios)\n1. Dios es el creador providente de todas las cosas.\nDios es la primera y máxima realidad. Es un Dios verdadero, vivo, creador del cielo y de la\ntierra, omnipresente y omnisciente. Nos creó y estableció una alianza con nosotros. Le\nllamamos Padre porque lo reconocemos como una autoridad trascendente que nos ama.\n2. La dignidad de la persona deriva de su condición de hijo de Dios.\nDios creó al ser humano a Su imagen: libre y responsable. Nuestra dignidad inherente deriva\nde nuestra filiación divina y no de nuestras características físicas, estatus social, posesiones\nmateriales u otros atributos. Estamos llamados por Dios a ser compasivos y caritativos unos\ncon otros, partiendo, no de la imposición, sino de acciones libres y responsables.\n3. Existe la verdad y el hombre es capaz de conocerla.\nLas personas, dotadas de inteligencia, somos capaces de aprehender la verdad sobre el\nmundo que nos rodea, aunque siempre de forma imperfecta. A través del estudio y del diálogo\ncon otras personas, discernimos la verdad. La verdad revelada por Dios nos permite\naproximarnos al conocimiento de Dios y su creación.\n4. La persona es libre, responsable y social por naturaleza.\nLas personas expresamos, a través de nuestros actos, nuestras preferencias y capacidades\ncuando elegimos en libertad los bienes morales que nos potencian. Las personas libres y\nresponsables asumimos las consecuencias positivas y negativas de nuestras elecciones.\nSomos cocreadores de cultura, instituciones y riqueza, sobre todo cuando cooperamos\npacíficamente con otros. La cooperación entre las personas depende de la igualdad ante la ley,\nde la prueba y error como factor correctivo y así mismo, de la libertad (del mecanismo) de\nprecios que sintetizan información (informa) sobre la escasez relativa de los bienes y su\ndemanda.\n5. El pecado es una realidad.\nEl pecado es una realidad histórica que nos afecta en el tiempo y en el espacio. Los hombres\nno tenemos conocimiento perfecto de lo que ocurre a nuestro alrededor y solo podemos\natenernos al aprendizaje frente al conocimiento disperso de factores, necesidades y procesos.\nEs de mejor calidad la información que sustenta nuestras elecciones en un entorno libre que en\nun entorno coercitivo y centralizado, aunque nunca será perfecta. A veces, las personas\nelegimos el mal; pero si somos libres, podemos reconocer nuestra falta, pedir perdón y\nrectificar.\n6. El florecimiento material depende de la creación de riqueza.\n\nLas personas prosperan cuando producen, consumen e intercambian libremente con los\ndemás. Los intercambios voluntarios permiten a las personas expresar su naturaleza creativa.\nConvierten las transacciones que pudieran ser juegos de suma cero, donde la ganancia de uno\nes a costillas del otro, en transacciones mutuamente ventajosas. El florecimiento humano\nrequiere que la comunidad y sus gobernantes respeten los derechos de propiedad privada, la\nlibertad de contratos y el Estado de Derecho. Dichas instituciones potencian la creación de\nriqueza.\n7. Todos los seres humanos son iguales ante la ley.\nRecibimos de Dios los dones de la vida, la libertad y la propiedad. La igualdad ante la ley de los\ngobernados se inspira en la igualdad de todas las criaturas humanas a ojos de Dios Padre.\nMuchos textos constitucionales coinciden con la tradición judeocristiana en reconocer la\npropiedad, la vida y la libertad de los hombres, como derechos anteriores y superiores al\nestado. El principio de subsidiariedad fortalece al estado de derecho por cuanto busca evitar\nque el aparato gubernamental usurpe aquellas funciones que deben ser desempeñadas por la\npersona individual y las instituciones que le son más inmediatas, y porque reduce la asistencia\nestatal únicamente a aquellas instancias en que las personas individuales y las instituciones\nque le son más inmediatas no han sido capaces de desempeñar las funciones que les son\npropias.\n8. La familia es el fundamento de la sociedad.\nUna familia es una sociedad natural y el fundamento de la sociedad, cuyo derecho a existir es\nsustentado por la ley divina. La familia es una comunidad de personas conformada por padre,\nmadre e hijos. Las sagradas escrituras resaltan la relevancia de la familia: nos instan a honrar\na padre y a madre y describen como modelo a la Sagrada Familia, conformada por José, María\ny Jesús. Las personas que tienen vocación al matrimonio y a la paternidad reciben la gracia y\nacompañamiento de Dios para honrar el compromiso matrimonial a ser fiel y a honrar y respetar\na la pareja elegida, y para formar y educar a sus hijos en el amor y la fe.\n9. El futuro de la civilización depende de la cultura de la libertad.\nSi la persona humana tiene un origen y un destino trascendente, entonces un entorno cultural\nque reconoce esta verdad conduce al florecimiento humano. La cultura de la libertad y de la\nvida produce orden y armonía entre los miembros de la comunidad, y la familia es la principal\ntransmisora de dicha cultura. Con frecuencia, las personas creyentes entran en tensión con la\ncultura popular, o la cultura secular, la cual puede alejarnos de Dios, de lo bello y del bien, y\nsuele tomar matices intolerantes. Creemos que es necesario rescatar los valores\njudeocristianos que constituyen los cimientos de la civilización occidental, incluyendo el valor\ndel pluralismo y el respeto a quienes tienen convicciones diferentes a las nuestras.\nVALORES Y VIRTUDES\nVeracidad. Es la virtud que nos lleva a buscar, en todo y ante todo, la verdad y a defenderla\ncon valor. La persona veraz es sincera, honesta, franca y tiene buena fe. Sabe escuchar y\nrespetar las opiniones del prójimo.\n\nLibertad. La persona libre posee la facultad natural para pensar y actuar según su voluntad\nordenada al bien. Ser libre implica ser responsable.\nIntegridad. La persona íntegra es de una sola pieza: recta, confiable, coherente y honesta.\nPiensa lo que vive y vive lo que piensa.\nHumildad. La persona humilde se reconoce como un ser creado, herido por el pecado pero\namado infinitamente por Dios.\nTolerancia. La persona tolerante sabe que existen diferentes criterios y tiene capacidad de\ndebatir con el otro con paciencia y comprensión. Distingue entre el respeto a la persona y sus\nideas, creencias o prácticas, que pueden o no ser erróneas.\n\n\n\nP: ¿Qué es lo que instituto Fe y Libertad cree?\nR: Instituto Fe y Libertad cree en Dios como el creador providente de todas las cosas, en la dignidad de la persona humana, en la existencia de la verdad, en la libertad y responsabilidad de las personas, en el pecado como una realidad, en que el florecimiento material depende de la creación de riqueza, en que todos los seres humanos son iguales ante la ley, en que la familia es el fundamento de la sociedad y en que el futuro de la civilización depende de la cultura de la libertad.\n\nP: ¿De dónde deriva la dignidad de la persona?\nR: La dignidad de la persona deriva de su condición de hijo de Dios.\n\nP: ¿Qué es lo que hace que las personas sean libres y responsables?\nR: Las personas son libres y responsables por naturaleza.\n\nP: ¿Qué es el pecado?\nR: El pecado es una realidad histórica que nos afecta en el tiempo y en el espacio.\n\nP: ¿Cómo podemos discernir la verdad?\nR: A través del estudio y del diálogo con otras personas, discernimos la verdad. La verdad revelada por Dios nos permite aproximarnos al conocimiento de Dios y su creación.\n")
    
def mises(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = client.generation.create(
        engine="finetuned-gpt-neox-20b",
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

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
