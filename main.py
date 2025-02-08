import speech_recognition as sr
import pyttsx3 as tts
import os
import eel
from groq import Groq


# eel.init("www")
# eel.start('index.html', mode=None, host='localhost', block=True)
# os.system("start msedge.exe --app='http://localhost:8000/index.html'")


# # Ensure API key is correctly set
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set. Please set it as an environment variable.")

client = Groq(api_key=GROQ_API_KEY)

voice_num = int()

# # Initialize text-to-speech engine
engine = tts.init("sapi5")
voices = engine.getProperty("voices")
print(voices)

# # Set properties
engine.setProperty("voice", voices[1].id)
engine.setProperty('rate', engine.getProperty('rate') - 60)

def speak(text):
    """Function to speak out the text."""
    engine.say(text)
    engine.runAndWait()

def wish_me():
    """Function to greet the user."""
    speak("Hello Master! I am Allied MasterComputer. In short, AM. I am here to help you with your needs.")# I am Allied MasterComputer. In short, AM. I am here to help you with your needs.


if __name__ == "__main__":
    wish_me()

while True:
    voice_num = int(input(speak('which voice do you like 1. english 2. hindi')))

    if voice_num == 1:
        engine.setProperty('voice', voices[1].id)
        a = input(speak('do you like this voice'))
        if a == "yes":
            break
    elif voice_num == 2:
        engine.setProperty('voice', voices[2].id)
        a = input(speak('do you like this voice'))
        if a == 'yes':
            break




# # Initialize speech recognizer
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("\nListening... (Say 'exit' to stop)")
        try:
            audio_text = r.listen(source, timeout=5)  # Avoids infinite wait
            content = r.recognize_google(audio_text).lower()
            print("You said:", content)

            # Exit condition
            if "exit" in content:
                print("Exiting...")
                speak("Goodbye, Master!")
                break  # Stops the loop

            # Send text to Groq API
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": content}],
                model="llama-3.3-70b-versatile",
            )

            ai_response = chat_completion.choices[0].message.content
            print("AI Response:", ai_response)

            # Speak the response
            speak(ai_response)

        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError:
            print("Could not request results, check your internet connection.")
        except Exception as e:
            print(f"An error occurred: {e}")