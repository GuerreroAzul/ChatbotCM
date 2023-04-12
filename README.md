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

* [Descripción del proyecto](#Descripcion)
* [Estado del proyecto](#Estado)
* [Características de la aplicación y demostración](#Características)
* [Instalacion del proyecto](#Instalacion)
* [Acceso al proyecto](#Acceso)
* [Tecnologías utilizadas](#Tecnologías)
* [Desarrolladores del Proyecto](#Desarrolladores)
* [Licencia](#Licencia)
* [Conclusión](#Conclusión)

## :notebook: Descripción del proyecto

<p align="justify">Este es un proyecto de IA que consiste en la implementación de un chatbot con reconocimiento de texto. Utiliza varias bibliotecas como <b>Speech_Recognition</b> y <b>NLTK</b> para procesamiento del lenguaje natural, tokenización, análisis sintáctico y lematización, entre otras cosas. El chatbot está entrenado con pares de patrones de respuestas para poder comprender el lenguaje natural y responder a las preguntas de los usuarios en el área de la medicina. El chatbot también permite al usuario elegir si desea realizar la consulta hablando o escribiendo.</p>

<p align="justify">Este código es un programa de chatbot que utiliza reconocimiento de voz para permitir al usuario hablar con el chatbot. El chatbot es capaz de proporcionar información médica básica en respuesta a las preguntas del usuario.</p>   

## :closed_book: Estado del proyecto

Este se encuentra en estado de testeo y pruebas, de lo cual le falta realizar mas el entrenamiento de la IA.

## :eight_spoked_asterisk: Características de la aplicación y demostración

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
pip install pyaudio SpeechRecognition nltk numpy && pip3 install flask
```

## :rocket: Acceso al proyecto
**Paso 1:** En la carpeta raiz ejecutamos la terminal el siguiente comando:
```Shell
python3 admin.py
```
**Paso 2:** Selecionaos ***Ctrl + Clic izquierdo*** en la direccion: **"127.0.0.1:5000"** para acceder al proyecto:
![Terminal](https://user-images.githubusercontent.com/69611007/231316081-6628c1e3-21c2-4d28-bf91-04fb8992d998.png)

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

## :busts_in_silhouette: Desarrolladores del Proyecto
* **Elsy Paola Amaya Lazo** - 201910040094
* **Orlin Fabricio Lagos**  - 201710110523

## :page_facing_up: Licencia
Python se desarrolla bajo una licencia de Open source o código abierto aprobada por OSI, por lo que se puede usar y distribuir libremente, incluso para uso comercial.
[CNRI OPEN SOURCE LICENSE AGREEMENT](https://opensource.org/license/cnri-python/)
[PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2](https://opensource.org/license/pythonsoftfoundation-php/)

## :bookmark_tabs: Conclusión
