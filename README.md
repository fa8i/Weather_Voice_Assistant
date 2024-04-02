Voice-Activated Weather Assistant
This Python script serves as a voice-activated weather assistant. It utilizes speech recognition to understand user input and OpenWeatherMap API to fetch weather information based on the user's query.

Features
Speech Recognition: Utilizes the speech_recognition library to convert spoken words into text.
Text-to-Speech: Employs pyttsx3 to convert text responses into speech, providing auditory feedback to the user.
Weather Information: Retrieves weather data for a specified location using the OpenWeatherMap API.
Interactive Voice Interaction: Engages in interactive voice communication with the user to provide weather updates.

Setup
1. Install the required Python libraries:
   pip install speech_recognition pyttsx3 requests
2. Sign up for an API key at OpenWeatherMap and replace "TU API KEY" with your actual API key in the code.
3. Run the script:
   python weather_assistant.py
4. Follow the prompts and speak your query to get weather information.

Usage
1. Upon running the script, the voice assistant will ask if you want to know the weather of any place.
2. Speak your query, mentioning keywords like "tiempo", "clima", or "temperatura", followed by the location you're interested in.
3. The assistant will recognize your query, retrieve the weather information, and speak out the temperature and weather conditions for the specified location.

Notes
The script is currently set to recognize speech in Spanish. Modify the language parameter in 'recognizer.recognize_google()' for other languages.
Ensure a stable internet connection for accurate weather data retrieval from the OpenWeatherMap API

Contributions
Contributions are welcome! Feel free to submit pull requests with enhancements, bug fixes, or new features to improve the functionality and user experience of the voice-activated weather assistant

Disclaimer: This project is for educational and personal use only. Please ensure compliance with the terms of service of any third-party services utilized in this script, such as OpenWeatherMap.
