from flask import Flask, render_template, request, redirect, url_for, session, flash
app = Flask(__name__, template_folder='site', static_folder='file')
app.secret_key = '\xef\xd2-\xe8\x91\xb9\xae\xef\xdfz\xb3\x15[\xcc\xad\x1fh@\xab\xf1\x1e\x15\x89\x02'

import Fnpy.FnSQLite3 as SQL
from Fnpy.FnSpeechRecognition import Speed_to_text as Speed
from Fnpy.FnNLTK import Response

# Función para verificar si el usuario ha iniciado sesión
def check_login():
    if 'user_id' in session:
        return True
    return False

# Página de inicio de sesión
@app.route('/login')
def login():
    return render_template('login.html')

# Función de inicio de sesión
@app.route('/login', methods=['POST'])
def login_post():
    # Obtener los valores del formulario
    user_name = request.form['username']
    password = request.form['password']
    
    if SQL.Login(user_name, password, session):
        return redirect(url_for('home'))
    else:
        flash('Datos del usuario incorrecto o inactivo ')
        return render_template('login.html', error='Usuario o contraseña incorrectos')

# Cerrar sesión
@app.route('/logout')
def logout():
    # Eliminar la información del usuario de la sesión
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('rol', None)
    flash('Ha cerrado sesión.')
    return redirect(url_for('login'))

@app.route('/')
def index():
    # Verificar si el usuario ha iniciado sesión
    SQL.ClearChat()
    SQL.NewChat('../file/icon/chatbot.png','Hola, Soy un chatbot diseñado para proporcionar información médica básica.', 'bot')
    chats = SQL.Chat()
    return render_template('index.html', chats=chats)

@app.route('/home')
def home():
    # Verificar si el usuario ha iniciado sesión
    if not check_login():
        return redirect(url_for('login'))
    
    # Obtener la cadena de búsqueda ingresada por el usuario
    search = request.args.get('search')
    questions = SQL.Question(search)
    return render_template('questions.html', questions=questions)

#Guardar Nuevas Preguntas
@app.route('/question', methods=['POST'])
def save_question():
    question = request.form['question']
    answer = request.form['answer']

    SQL.NewQuestion(question, answer)
    flash('La pregunta ha sido guardada.')

    # Redirigir al usuario a la página de preguntas
    return redirect(url_for('home'))

@app.route('/question/delete/<int:id>', methods=['POST'])
def delete_question(id):
    # Verificar si el usuario ha iniciado sesión
    if not check_login():
        return redirect(url_for('login'))
    
    SQL.DelQuestion(id)
    flash('La pregunta ha sido deshabilitada.')

    # Redirigir al usuario a la página de preguntas
    return redirect(url_for('home'))

@app.route('/edit_question_modal', methods=['POST'])
def edit_question_modal():
     # Verificar si el usuario ha iniciado sesión
    if not check_login():
        return redirect(url_for('login'))
    
    # Obtener los valores del formulario
    question_id = request.form['id1']
    question = request.form['question1']
    answer = request.form['answer1']

    SQL.EditQuestion(question, answer, question_id)

    flash('La pregunta ha sido actualizada.')
    # Redirigir a la página principal
    return redirect(url_for('home'))


@app.route('/error')
def error():
     # Verificar si el usuario ha iniciado sesión
    if not check_login():
        return redirect(url_for('login'))

    errors = SQL.Errors()

    return render_template('errors.html', errors=errors)

@app.route('/error/delete/<int:id>', methods=['POST'])
def delete_error(id):
    SQL.DelErrors(id)

    flash('La pregunta ha sido eliminada.')
    # Redirigir al usuario a la página de preguntas
    return redirect(url_for('error'))

@app.route('/user')
def user():
     # Verificar si el usuario ha iniciado sesión
    if not check_login():
        return redirect(url_for('login'))
    
     # Obtener la cadena de búsqueda ingresada por el usuario
    search = request.args.get('search')

    users = SQL.Users(search)

    return render_template('users.html', users=users)

@app.route('/save-user', methods=['POST'])
def save_user():
    # Obtener los valores del formulario
    user_name = request.form['username']
    password = request.form['password']
    rol = request.form['rol']

    SQL.NewUsers(user_name, password, rol)

    flash('El usuario ha sido guardado.')
    return redirect(url_for('user'))

@app.route('/user/delete/<int:id>', methods=['POST'])
def delete_user(id):
    # Conectarse a la base de datos
    
    SQL.DelUsers(id)

    flash('El usuario ha sido deshabilitado.')
    # Redirigir al usuario a la página de preguntas
    return redirect(url_for('user'))

@app.route('/edit_user_modal', methods=['POST'])
def edit_user_modal():
    # Obtener los valores del formulario
    user_id = request.form['id1']
    user= request.form['username1']
    rol = request.form['rol1']

    SQL.EditUsers(user, rol, user_id)
   
    flash('El usuario ha sido actualizado.')
    # Redirigir a la página principal
    return redirect(url_for('user'))

@app.route('/edit_pass_modal', methods=['POST'])
def edit_pass_modal():
    # Obtener los valores del formulario
    user_id = request.form['id2']
    password= request.form['password2']

    SQL.EditPassword(password, user_id)

    flash('El password ha sido actualizado.')
    # Redirigir a la página principal
    return redirect(url_for('user'))

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        choice = request.form['choice']
        if choice == 'h':
            textbox = Speed()
            return render_template('index.html', textbox=textbox)
        elif choice == 'e':
            transcript = request.form['text']
            Response(transcript)
            chats = SQL.Chat()
            return render_template('index.html', chats=chats)
        else:
            return "Opción inválida. Por favor, seleccione 'h' para hablar, 'e' para escribir."

if __name__ == '__main__':
    app.run(debug=True)
