from voice_utils import speak, listen
from commands import process_command

# Función principal del asistente
def main():
    speak("Hola, soy tu asistente de voz. ¿En qué puedo ayudarte?")
    while True:
        command = listen()
        if command:
            response = process_command(command)
            speak(response)
            if "adiós" in command or "salir" in command:
                break

if __name__ == "__main__":
    main()
    