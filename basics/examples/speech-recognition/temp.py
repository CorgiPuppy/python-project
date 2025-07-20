import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

with microphone as source:
    print("Say patient's name..")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="ru-Ru")
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Speech isn't recognized")
except sr.RequestError as e:
    print(f"Service error; {e}")

with microphone as source:
    print("Say patient's name..")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_sphinx(audio, language="ru-RU")
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Speech isn't recognized")
except sr.RequestError as e:
    print(f"Service error; {e}")