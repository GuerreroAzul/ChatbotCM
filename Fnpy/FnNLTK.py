import nltk
from nltk.chat.util import Chat, reflections
import sqlite3
from unidecode import unidecode
import re
import Fnpy.FnSQLite3 as SQL
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DB = 'data/chatbot.db'

# conecta con la base de datos y obtiene las preguntas y respuestas para el entrenamiento
def get_training_data():
    #Conexion a la consulta de preguntas
    conn = sqlite3.connect(DB)
    cursor = conn.execute("SELECT question, answer FROM question WHERE state = 'Activo'")

    training_data = []
    for row in cursor:
        training_data.append({"question": row[0], "answer": row[1]})
    return training_data

# preprocesamiento de texto para el entrenamiento
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = unidecode(text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('spanish'))
    tokens = [t for t in tokens if not t in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)

# entrena el modelo de chatbot
def train_chatbot():
    training_data = get_training_data()
    preprocessed_questions = [preprocess_text(d['question']) for d in training_data]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(preprocessed_questions)
    chatbot = {"vectorizer": vectorizer, "vectors": vectors, "data": training_data}
    return chatbot

# responde a la pregunta del usuario utilizando el modelo entrenado
def Response(user_question, chatbot):
    user_question = preprocess_text(user_question)
    user_vector = chatbot["vectorizer"].transform([user_question])
    similarities = cosine_similarity(user_vector, chatbot["vectors"]).flatten()
    index = similarities.argsort()[-1]
    if similarities[index] == 0:
        return "Lo siento, no entiendo tu pregunta."
    else:
        return chatbot["data"][index]["answer"]

# entrena el modelo de chatbot y lo utiliza para responder a preguntas
def Chat(transcript):
    chatbot = train_chatbot()
    response = Response(transcript, chatbot)
    if str(response) == "Lo siento, no entiendo tu pregunta.":
        SQL.NewErrors(transcript)
        SQL.NewChat('../file/icon/usuario.png', transcript, 'user')
        SQL.NewChat('../file/icon/chatbot.png', response, 'bot')
    else:
        SQL.NewChat('../file/icon/usuario.png', transcript, 'user')
        SQL.NewChat('../file/icon/chatbot.png', response, 'bot')