import wolframapha
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 200)


def speak( audio ):
    """Speak out the given audio string."""
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = ""
    requester = wolframapha.client(apikey)
    requested = requester.query(query)

    try :
        answer = next(requested.results)
        return answer
    except :
        speak("The value is not answerable")

    def Calc(query):
        Term = str(query)
        Term = Term.replace("jarvis", "")
        Term = Term.replace("multiply", "*")
        Term = Term.replace("plus", "+")
        Term = Term.replace("divide", "-")
        Term = Term.replace("divide", "/")

        Final = str(Term)
        try:
            results = WolfRamAlpha(Final)
            print(f"{result}")
            speak(result)

        except :
            speak("The value is not answerable")
