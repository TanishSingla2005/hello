import speech_recognition as sr

def listen_and_convert():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙 Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("📝 You said:", text)
    except sr.UnknownValueError:
        print("😕 Sorry, could not understand your voice.")
    except sr.RequestError:
        print("⚠ Could not request results from Google Speech Recognition.")

listen_and_convert()