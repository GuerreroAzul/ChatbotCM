#! /bin/bash
clear
echo Buscando actualizaciones...
sleep 3s

sudo apt-get update -y && sudo apt-get upgrade -y

echo --------------------------------
echo Presione enter para continuar...
read
clear
echo Instalando Complemento de Python...
sleep 3s

sudo apt install build-essential python3-pip libffi-dev python3-dev python3-setuptools libssl-dev -y

echo --------------------------------
echo Presione enter para continuar...
read
clear
echo Instalando PyAudio...
sleep 3s

sudo apt install libasound-dev portaudio19-dev -y

echo --------------------------------
echo Presione enter para continuar...
read
clear
echo Instalando Librerias Python...
sleep 3s

pip install pyaudio SpeechRecognition nltk numpy && pip3 install flask && pip install -U scikit-learn

echo --------------------------------
echo Presione enter para continuar...
read
clear
echo Instalacion finalizada...
sleep 3s
clear
