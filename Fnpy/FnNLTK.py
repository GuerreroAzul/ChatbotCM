import nltk
from nltk.chat.util import Chat, reflections
import sqlite3
from unidecode import unidecode
import re
from Fnpy.FnSQLite3 import NewErrors, NewChat

def Response(transcript):
        conn = sqlite3.connect('data/chatbot.db')

        # ejecuta una consulta SQL para obtener las preguntas y respuestas de la tabla
        cursor = conn.execute("SELECT question, answer FROM question WHERE state = 'Activo'")

        # crea una lista de pares de preguntas y respuestas
        pairs = [(row[0], [row[1]]) for row in cursor]
        chatbot = Chat(pairs, reflections)


        #ELIMINACION DE SIGNO DE PUNTUACION
        transcript = re.sub(r'[^\w\s]', '', transcript)
        transcript = unidecode(transcript)
        
        # PROCESAMIENTO DEL TEXTO NLKT
        tokens = nltk.word_tokenize(transcript)
        response = chatbot.respond(transcript)

        if str(response) == 'None':
            response = "Lo siento, no entiendo tu pregunta."
            NewErrors(transcript)
            NewChat('User: ', transcript)
            NewChat('Chatbot: ', response)
        else:
            NewChat('User: ', transcript)
            NewChat('Chatbot: ', response)