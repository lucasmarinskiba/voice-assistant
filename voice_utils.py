import speech_recognition as sr
import pyttsx3

# Inicializar el reconocedor de voz y el motor de texto a voz
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Configurar la voz (opcional)
def configure_voice(voice_id=0):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)

# Función para hablar
def speak(text):
    print(f"Asistente: {text}")
    engine.say(text)
    engine.runAndWait()

# Función para escuchar
def listen():
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="es-ES")
            print(f"Tú: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("No entendí lo que dijiste. ¿Puedes repetirlo?")
            return None
        except sr.RequestError:
            speak("Hubo un error al conectarse al servicio de reconocimiento de voz.")
            return None