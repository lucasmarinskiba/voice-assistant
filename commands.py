from datetime import datetime

# Función para procesar comandos
def process_command(command):
    if "hola" in command:
        return "¡Hola! ¿Cómo estás?"
    elif "hora" in command:
        now = datetime.now()
        return f"Son las {now.strftime('%H:%M')}"
    elif "fecha" in command:
        now = datetime.now()
        return f"Hoy es {now.strftime('%d/%m/%Y')}"
    elif "adiós" in command or "salir" in command:
        return "Hasta luego. ¡Que tengas un buen día!"
    else:
        return "No entendí ese comando. ¿Puedes intentar con otra cosa?"