import sqlite3

# conecta con la base de datos
conn = sqlite3.connect('chatbot.db')

# crea una tabla para guardar las preguntas y respuestas
conn.execute('''CREATE TABLE IF NOT EXISTS question
             (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, answer TEXT, state TEXT);''')

conn.execute('''CREATE TABLE IF NOT EXISTS error
             (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, state TEXT);''')

conn.execute('''CREATE TABLE IF NOT EXISTS user
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
     user_name TEXT,
     password TEXT,
     rol TEXT,
     state TEXT);''')

conn.execute('''CREATE TABLE IF NOT EXISTS chat
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
	Tipo TEXT,
	Texto INTEGER,
    Tipo2 INTEGER);''')

# guarda los cambios en la base de datos
conn.commit()

# cierra la conexión con la base de datos
conn.close()

