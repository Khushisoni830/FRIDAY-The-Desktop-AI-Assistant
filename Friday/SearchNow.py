import speech_recognition as sr  # Import the module as 'sr' for recognition functions
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


def takeCommand():
    """Take microphone input from the user and return it as a string."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 250  # Adjust based on your environment
        audio = r.listen(source, timeout=10, phrase_time_limit=10)

        try:
            print("Understanding...")
            googly = r.recognize_google(audio, language='en-in')
            print(f"You said: {googly}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that. Please say that again.")
            return "None"
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return "None"
        except Exception as e:
            print(f"An error occurred: {e}")
            return "None"

    return googly


query = takeCommand().lower()

# Initialize the text-to-speech engine with the correct driver
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak( audio ):
    """Speak out the given audio string."""
    engine.say(audio)
    engine.runAndWait()


def searchGoogle( googly ):
    if "google" in googly:
        import wikipedia as googleScrap
        googly = googly.replace("jarvis", "")
        googly = googly.replace("search goole", "")
        googly = googly.replace("google", "")
        speak("This is what i found on ggogle")

        try:
            pywhatkit.search(googly)
            result = googleScrap.summery(googly, 1)
            speak(result)

        except:
            speak("No Speakable output available")


def searchYoutube( googly ):
    if "youtube" in googly:
        speak("This is what i found for your search!! ")
        googly = googly.replace("jarvis", "")
        googly = googly.replace("search youtube", "")
        googly = googly.replace("youtube", "")
        web = "https://www.youtube.com/results?search_query=" + googly
        webbrowser.open(web)
        pywhatkit.playonyt(googly)
        speak("Done, Sir")


def searchWikipedia( googly ):
    if "wikipedia" in googly:
        speak("Searching from wikipedia...")
        googly = googly.replace("jarvis", "")
        googly = googly.replace("search wkipedia", "")
        googly = googly.replace("wikipedia", "")
        results = wikipedia.summary(googly, sentences=2)
        speak("According to wikipedia..")
        print(results)
