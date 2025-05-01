import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
from datetime import datetime, timedelta

# Initialize the text-to-speech engine with the correct driver
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    """Speak out the given audio string."""
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    """Take microphone input from the user and return it as a string."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 250  # Adjust based on your environment
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)

        try:
            print("Understanding...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that. Please say that again.")
            return "None"
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return "None"
        except Exception as e:
            print(f"An error occurred: {e}")
            return "None"

    return query


# Get the current time for scheduling the message
strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))


def sendMessage():
    """Send a WhatsApp message based on voice input."""
    speak("Who do you want to message?")
    print('''Choose an option by speaking:
    1. Khushi
    2. Monesh Bhaiya''')
    contact_choice = takeCommand().lower()

    if "khushi" in contact_choice or "one" in contact_choice:
        recipient = "+918305141351"
    elif "monesh" in contact_choice or "two" in contact_choice:
        recipient = "+919516082136"
    else:
        speak("Sorry, I didn't understand the recipient. Please try again.")
        return

    speak("What is the message?")
    print("Listening for the message...")
    message = takeCommand()

    if message == "None":
        speak("No message detected. Aborting.")
        return

    try:
        pywhatkit.sendwhatmsg(recipient, message, time_hour=strTime, time_min=update)
        speak("Message has been scheduled. Please check WhatsApp to confirm.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, I was unable to send the message.")
        breakpoint()


