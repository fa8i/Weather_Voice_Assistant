import speech_recognition as sr
import pyttsx3
import requests
import re

# Inicializar el motor de texto a voz
engine = pyttsx3.init()
engine.setProperty("rate", 200)
engine.setProperty("voice", "spanish")

# Inicializar el reconocimiento de voz
recognizer = sr.Recognizer()


def get_weather(city):          # Definir la función para obtener el clima
    api_key = "TU API KEY"  # Reemplaza con tu API Key de OpenWeatherMap
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=es&units=metric"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        return f"La temperatura en {city} es {temperature}°C y el clima es {weather}."
    else:
        return "No pude obtener la información del clima."


def voice_assistant():          # Definir la función para interactuar con el asistente de voz
    with sr.Microphone() as source:
        try:
            engine.say("¿Te interesa conocer el clima de algun lugar?")
            engine.runAndWait()
            print("Puedes hablar...")
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="es-ES")
            print(f"Tú dijiste: {text}")
            patterns = ["tiempo", "clima", "temperatura"]
            for pattern in patterns:
                if pattern in text:
                    city = re.findall(r"en (\w+)", text)[0]
                    print(f"La localizacion es: {city}")
                    weather_response = get_weather(city)
                    engine.say(weather_response)
                else:
                    pass
        except sr.UnknownValueError:
            engine.say("Lo siento, no pude entender lo que dijiste.")
        except sr.RequestError:
            engine.say("Lo siento, hubo un error al procesar tu solicitud.")

    engine.runAndWait()


def main():             # Definir la función principal
    while True:
        voice_assistant()


if __name__ == "__main__":
    main()
