#IMPORTACION DE LIBRERIAS
import speech_recognition as sr     #Esta biblioteca proporciona una interfaz fácil de usar para trabajar con varios motores de reconocimiento de voz.

#DECLARACION DE VARIABLES
r = sr.Recognizer()

def Speed_to_text():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  #Ajusta al ruido ambiental
        try:
            audio = r.listen(source, timeout=5) #Tiempo de espera de 5 segundos
        except sr.WaitTimeoutError:
            transcript = "No se detectó entrada de audio, Intente de nuevo por favor."
            return transcript
    try:
        transcript = r.recognize_google(audio, language='es-ES', show_all=False)
        return transcript
    except sr.UnknownValueError:
        transcript = "No se pudo entender el audio, intente de nuevo por favor."
        return transcript