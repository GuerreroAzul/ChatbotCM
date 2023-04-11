#Importacion de librerias.
import sqlite3
import hashlib

DB = 'data/chatbot.db'

def Login(user_name, password, session):
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # Encriptar la contraseña
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Verificar si el usuario existe en la tabla user
    cursor.execute("SELECT id, user_name, rol FROM user WHERE user_name = ? AND password = ? AND state = 'Activo'", (user_name, hashed_password))
    user = cursor.fetchone()

    if user:
        # Iniciar sesión
        session['user_id'] = user[0]
        session['user_name'] = user[1]
        session['rol'] = user[2]
        conn.close()
        return True
    else:
        conn.close()
        return False

def Question(search):
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    if search:
        # Buscar las preguntas que contienen la cadena de búsqueda
        cursor.execute("SELECT * FROM question WHERE question LIKE ?", ('%' + search + '%',))
    else:
        # Obtener todas las preguntas
        cursor.execute("SELECT * FROM question")

    questions = cursor.fetchall()
    conn.close()
    return questions

def NewQuestion(question, answer):
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # Insertar los datos en la tabla question
    cursor.execute("INSERT INTO question (question, answer, state) VALUES (?, ?, 'Activo')", (question, answer))

    # Guardar los cambios
    conn.commit()
    conn.close()

def EditQuestion(question, answer, question_id):
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    # Actualizar la pregunta en la base de datos
    cursor.execute('UPDATE question SET question = ?, answer = ?, state="Activo" WHERE id = ?', (question, answer, question_id))

    # Guardar los cambios en la base de datos
    conn.commit()
    conn.close()

def DelQuestion(id):
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # Actualizar el estado de la pregunta a "Inactivo"
    cursor.execute("UPDATE question SET state = 'Inactivo' WHERE id = ?", (id,))

    # Guardar los cambios
    conn.commit()
    conn.close()

def Errors():
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
   
    cursor.execute("SELECT id, question FROM error WHERE state = 'Activo'")
    errors= cursor.fetchall()
    conn.close()
    return errors

def NewErrors(transcript):
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # Insertar los datos en la tabla error
    cursor.execute('''INSERT INTO error (question,state) VALUES (?, ?)''', (str(transcript), 'Activo'))

    # Guardar los cambios
    conn.commit()
    conn.close()

def DelErrors(id):
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # Actualizar el estado de la pregunta a "Inactivo"
    cursor.execute("UPDATE error SET state = 'Inactivo' WHERE id = ?", (id,))
    
    # Guardar los cambios
    conn.commit()
    conn.close()

def Users(search):
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    if search:
        # Buscar las preguntas que contienen la cadena de búsqueda
        cursor.execute("SELECT * FROM user WHERE user_name LIKE ?", ('%' + search + '%',))
    else:
        cursor.execute("SELECT * FROM user")

    users= cursor.fetchall()
    conn.close()
    return users

def NewUsers(user_name, password, rol):
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor() 

    # Encriptar la contraseña
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Insertar el nuevo registro en la tabla user
    cursor.execute("INSERT INTO user (user_name, password, rol, state) VALUES (?, ?, ?, 'Activo')", (user_name, hashed_password, rol))
    conn.commit()
    conn.close()

def EditUsers(user, rol, user_id):
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor() 

    # Actualizar la pregunta en la base de datos
    cursor.execute('UPDATE user SET user_name = ?, rol = ?, state = "Activo" WHERE id = ?', (user, rol, user_id))

    # Guardar los cambios en la base de datos
    conn.commit()
    conn.close()

def DelUsers(id):
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor() 

     # Actualizar el estado de la pregunta a "Inactivo"
    cursor.execute("UPDATE user SET state = 'Inactivo' WHERE id = ?", (id,))

    # Guardar los cambios
    conn.commit()
    conn.close()

def EditPassword(password, user_id):
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor() 

    # Encriptar la contraseña
    new_password = hashlib.sha256(password.encode()).hexdigest()

    # Actualizar la pregunta en la base de datos.
    cursor.execute('UPDATE user SET password = ? WHERE id = ?', (new_password, user_id))

    # Guardar los cambios en la base de datos.
    conn.commit()
    conn.close()

def Chat():
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor() 

    cursor.execute("SELECT Tipo, Texto FROM chat")

    chat = cursor.fetchall()
    conn.close()
    return chat

def NewChat(tipo, texto):
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor() 

    # Insertar el nuevo registro en la tabla chat
    cursor.execute("INSERT INTO chat (Tipo, Texto) VALUES (?, ?)", (tipo, texto))
    conn.commit()
    conn.close()


def ClearChat():
    # Conectarse a la base de datos
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM chat WHERE id>1")
    conn.commit()
    conn.close()