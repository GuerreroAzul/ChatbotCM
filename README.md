<P align="center"><img src="https://user-images.githubusercontent.com/69611007/231231036-e0166da3-1704-4106-a0ec-04782f7e0c52.png"></P>

# ChatbotCM - Chatbot conversacional sobre consultas medicas

![Universidad](https://img.shields.io/badge/Universidad-Universidad%20Tecnol%C3%B3gica%20de%20Honduras-blue)
![Materia](https://img.shields.io/badge/Asignatura-Inteligencia%20Artificial%20(IAE--0611)-blue)
![Catedratico](https://img.shields.io/badge/Catedratico-Ing.%20Wilson%20Octaviano%20Villanueva%20Castillo-blue)

![Sistema](https://img.shields.io/badge/System-Debian%2011.5.0%20amd64-blueviolet)
![Python](https://img.shields.io/badge/Python-v3.9-green)
![License](https://img.shields.io/badge/License-CNRI%20OSI%20Python-green)
![Estado](https://img.shields.io/badge/Status-Alpha-green)
![Version](https://img.shields.io/badge/Stable-v.0.3.2-green)

## Índice

1. [Descripción del proyecto](#A)
3. [Estado del proyecto](#B)
4. [Características de la aplicación y demostración](#C)
5. [Instalacion del proyecto](#D)
6. [Acceso al proyecto](#E)
7. [Tecnologías utilizadas](#F)
8. [Desarrolladores del Proyecto](#G)
9. [Licencia](#H)
10. [Conclusión](#I)

<a name="A"></a>
## :notebook: Descripción del proyecto

<p align="justify">Este es un proyecto de IA que consiste en la implementación de un chatbot con reconocimiento de texto. Utiliza varias bibliotecas como <b>Speech_Recognition</b> y <b>NLTK</b> para procesamiento del lenguaje natural, tokenización, análisis sintáctico y lematización, entre otras cosas. El chatbot está entrenado con pares de patrones de respuestas para poder comprender el lenguaje natural y responder a las preguntas de los usuarios en el área de la medicina. El chatbot también permite al usuario elegir si desea realizar la consulta hablando o escribiendo.</p>

<p align="justify">Este código es un programa de chatbot que utiliza reconocimiento de voz para permitir al usuario hablar con el chatbot. El chatbot es capaz de proporcionar información médica básica en respuesta a las preguntas del usuario.</p>

<a name="B"></a>
## :closed_book: Estado del proyecto

Este se encuentra en estado de testeo y pruebas, de lo cual le falta realizar mas el entrenamiento de la IA.

<a name="C"></a>
## :eight_spoked_asterisk: Características de la aplicación y demostración

### Chatbot
![image](https://user-images.githubusercontent.com/69611007/231585789-afa3a07b-9750-469e-b133-2ba1044e5d70.png)

### Interfaz de entrada
![image](https://user-images.githubusercontent.com/69611007/231588039-305b41ca-b125-401c-8ff9-7df6a9030cc5.png)

### Control de preguntas
![image](https://user-images.githubusercontent.com/69611007/231588207-87f9238b-1b2a-46b3-81f3-333eb6dbbe8b.png)

### Control de Nuevas Preguntas
![image](https://user-images.githubusercontent.com/69611007/231588613-4f85cbed-acbd-4961-bb55-f731ec2be9d8.png)

### Control de Usuarios
![image](https://user-images.githubusercontent.com/69611007/231588614-80f76621-f721-410a-b1f8-abdd08adc257.png)

<a name="D"></a>
## :wrench: Instalacion del proyecto
**Paso 1:** Descargar el proyecto desde el siguiente enlace: [ChatbotCM](https://github.com/GuerreroAzul/ChatbotCM.git)

**Paso 2:** Actualizamos los repositorios del equipo.
```Shell
sudo apt-get update -y && sudo apt-get upgrade -y
```

**Paso 3:** Instalamos complementos de Python.
```Shell
sudo apt install build-essential python3-pip libffi-dev python3-dev python3-setuptools libssl-dev -y
```

**Paso 4:** Instalamos la libreria PyAudio.
```Shell
sudo apt install libasound-dev portaudio19-dev -y
```

**Paso 4:** Instalamos las librerias usadas en el proyecto.
```Shell
pip install pyaudio SpeechRecognition nltk numpy && pip3 install flask && pip install -U scikit-learn
```

<a name="E"></a>
## :rocket: Acceso al proyecto
**Paso 1:** En la carpeta raiz ejecutamos la terminal el siguiente comando:
```Shell
python3 admin.py
```
**Paso 2:** Selecionamos ***Ctrl + Clic izquierdo*** en la direccion: **"127.0.0.1:5000"** para acceder al proyecto:
![Terminal](https://user-images.githubusercontent.com/69611007/231316081-6628c1e3-21c2-4d28-bf91-04fb8992d998.png)

![image](https://user-images.githubusercontent.com/69611007/231585675-0905f86c-63c3-4d32-a659-a5d447b7455d.png)

<a name="F"></a>
## :books: Tecnologías utilizadas

### ***Lenguaje de Programación:***
* **Python v.3.9:** Es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software, la ciencia de datos y el machine learning (ML). Los desarrolladores utilizan Python porque es eficiente y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes.

### ***Firmware y librerias externas:***
* **Regex:** Es un módulo de Python que proporciona operaciones de coincidencia de expresiones regulares similares a las que se encuentran en Perl. Es una herramienta poderosa para trabajar con datos de texto y le permite buscar, coincidir y manipular cadenas utilizando expresiones regulares.
* **SpeechRecognition:** Es una librería de Python para realizar reconocimiento de voz, que es el proceso de convertir audio hablado en texto. Admite varios motores de reconocimiento de voz, incluidos Google Speech Recognition, Microsoft Bing Voice Recognition y otros.
* **NLTK:** Significa Natural Language Toolkit, y es una librería de Python para trabajar con datos de lenguaje humano, incluidos datos de texto. Proporciona una amplia gama de herramientas y recursos para tareas como tokenización, reducción de palabras a su raíz, etiquetado, análisis sintáctico y más.
* **Flask:** Para la creación y ejecución de la aplicación web.
* **Unicode:** Para convertir caracteres a su representación ASCII equivalente.

### ***Entornos de desarrollo:***
* **Visual Studio Code:** Es un editor de código fuente desarrollado por Microsoft para Windows, Linux, macOS y Web. Incluye soporte para la depuración, control integrado de Git, resaltado de sintaxis, finalización inteligente de código, fragmentos y refactorización de código.
### ***Desarrollo de interfaz:***
* **HTML5:** Siglas en inglés de HyperText Markup Language, hace referencia al lenguaje de marcado para la elaboración de páginas web.

* **CSS:** En español «Hojas de estilo en cascada», es un lenguaje de diseño gráfico para definir y crear la presentación de un documento estructurado escrito en un lenguaje de marcado.

### ***Base de datos:***
* **SQLite:** SQLite es un sistema de gestión de bases de datos relacional compatible con ACID, contenida en una relativamente pequeña (~275 kiB) biblioteca escrita en C. SQLite es un proyecto de dominio público creado por D. Richard Hipp.

<a name="G"></a>
## :busts_in_silhouette: Desarrolladores del Proyecto
* **Elsy Paola Amaya Lazo** - 201910040094
* **Orlin Fabricio Lagos**  - 201710110523

<a name="H"></a>
## :page_facing_up: Licencia
Python se desarrolla bajo una licencia de Open source o código abierto aprobada por OSI, por lo que se puede usar y distribuir libremente, incluso para uso comercial.

[CNRI OPEN SOURCE LICENSE AGREEMENT](https://opensource.org/license/cnri-python/)

[PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2](https://opensource.org/license/pythonsoftfoundation-php/)

<a name="I"></a>
## :bookmark_tabs: Conclusión

<p align="justify">Consiste en la creación de un chatbot que utiliza un modelo de aprendizaje automático para responder preguntas y una herramienta de reconocimiento de voz para permitir a los usuarios interactuar con el chatbot mediante comandos de voz. El archivo FnNLTK.py contiene el código para entrenar el modelo de chatbot utilizando el paquete Natural Language Toolkit (NLTK) y la biblioteca scikit-learn para crear un modelo de vectorización de términos de frecuencia de documentos invertidos (TF-IDF) y el cálculo de similitud coseno para encontrar la respuesta más adecuada a la pregunta del usuario. El archivo FnSpeechRecognition.py utiliza la biblioteca SpeechRecognition para capturar y transcribir los comandos de voz del usuario. En general, el proyecto tiene como objetivo facilitar la interacción con el chatbot a través de una herramienta de reconocimiento de voz y proporcionar respuestas precisas y relevantes utilizando un modelo de aprendizaje automático entrenado previamente.</p>
