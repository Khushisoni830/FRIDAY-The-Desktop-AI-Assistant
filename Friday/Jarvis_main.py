import os
import webbrowser
import pyttsx3
import speech_recognition as sr  # Use 'sr' for short notation
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
import random

# Function to take audio input for password
def take_audio_input():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        r1.adjust_for_ambient_noise(source)  # Adjusting for ambient noise
        print("Listening for the password...")
        r1.pause_threshold = 1
        r1.energy_threshold = 250  # Adjust based on your environment

        try:
            audio = r1.listen(source, timeout=10, phrase_time_limit=10)  # Listen for input
            print("Processing the audio input...")
            query = r1.recognize_google(audio, language='en-in')  # Google Speech API
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand that. Please try again.")
            return None  # Return None if not understood
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None  # Return None if there's a request error
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None  # Return None for other errors

# Main password checking code
for i in range(3):
    print(f"Attempt {i + 1} of 3")
    print("Please speak the password to open Jarvis.")

    # Take password input via voice command
    a = take_audio_input()

    if a is None:  # If no audio was understood, continue to the next attempt
        print("No input received. Please try again.")
        continue

    a = a.lower()  # Only convert to lowercase if a valid input was received

    # Reading the password from the file
    try:
        with open("password.txt", "r") as pw_file:
            pw = pw_file.read().strip()  # Strip to remove any extra spaces/newlines

        if a == pw:
            print("WELCOME SIR! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
            break
        elif i == 2 and a != pw:
            print("Access Denied. Exiting...")
            exit()
        else:
            print("Password incorrect. Try again.")
    except FileNotFoundError:
        print("Password file not found! Please make sure the file 'password.txt' exists.")
        exit()

# Initialize the text-to-speech engine with the correct driver
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 200)

def speak(audio):
    """Speak out the given audio string."""
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """Take microphone input from the user and return it as a string."""
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r1.pause_threshold = 1
        r1.energy_threshold = 250  # Adjust based on your environment
        try:
            audio = r1.listen(source, timeout=10, phrase_time_limit=10)
            print("Understanding...")
            query1 = r1.recognize_google(audio, language='en-in')
            print(f"You said: {query1}\n")
            return query1.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that. Please say that again.")
            return "none"
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return "none"
        except Exception as e:
            print(f"An error occurred: {e}")
            return "none"

def alarm(query):
    with open("Alarmtext.txt", "a") as timehere:
        timehere.write(query)
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand()

        if "wake up" in query or "uth jao" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand()

                if "go to sleep" in query:
                    speak("Ok Boss, you can call me anytime.")
                    break

                elif "hello" in query:
                    speak("Hello Boss, how are you?")
                elif "i am fine" in query:
                    speak("That's great Boss.")
                elif "how are you" in query:
                    speak("Perfect sir.")
                elif "thank you" in query:
                    speak("You're welcome, Boss.")

                elif "feeling tired" in query:
                    speak("Playing your favorite songs, sir.")
                    songs = [
                        "https://www.youtube.com/watch?v=dXBVvOZ_qnM&list=RDdXBVvOZ_qnM&start_radio=1",
                        "https://www.youtube.com/watch?v=D5dZAjn_8tw&list=RDdXBVvOZ_qnM&index=5",
                        "https://www.youtube.com/watch?v=kw4tT7SCmaY&list=RDdXBVvOZ_qnM&index=9",
                        "https://www.youtube.com/watch?v=zuvla6ABKbs&list=RDdXBVvOZ_qnM&index=13"
                    ]
                    webbrowser.open(random.choice(songs))

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused.")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played.")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted.")

                elif "volume up" in query:
                    pyautogui.press("volumeup")
                    speak("Turning volume up, sir.")

                elif "volume down" in query:
                    pyautogui.press("volumedown")
                    speak("Turning volume down, sir.")

                elif "save the file" in query:
                    pyautogui.hotkey('ctrl', 's')
                    speak("File is saved.")

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha, Calc
                    query = query.replace("calculate", "").replace("jarvis", "")
                    Calc(query)

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)

                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "temperature" in query or "weather" in query:
                    location = "temperature in bhopal"
                    url = f"https://www.google.com/search?q={location}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"Current {location} is {temp}.")

                elif "set an alarm" in query:
                    print("Input time example: 10 and 10 and 10")
                    speak("Set the time.")
                    a = input("Please tell the time: ")
                    alarm(a)
                    speak("Done, sir.")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}.")

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "").replace("jarvis", "")
                    speak("You told me to " + rememberMessage)
                    with open("Remember.txt", "a") as remember:
                        remember.write(rememberMessage + "\n")

                elif "what do you remember" in query:
                    try:
                        with open("Remember.txt", "r") as remember:
                            speak("You told me to " + remember.read())
                    except FileNotFoundError:
                        speak("You haven't told me to remember anything yet.")

                elif "recent tab" in query:
                    pyautogui.hotkey("ctrl", "shift", "t")
                    speak("Opened recent tab.")

                elif "shutdown the system" in query:
                    speak("Are you sure you want to shut down?")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no): ")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        speak("Shutdown cancelled.")

                elif "finally sleep" in query:
                    speak("Going to sleep Boss.")
                    exit()
