import pyttsx3
import datetime
import os

# Initialize the text-to-speech engine with the correct driver
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak( audio ):
    """Speak out the given audio string."""
    engine.say(audio)
    engine.runAndWait()


extractedtime = open("Alarmtext.txt", "rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt", "r+")
deletetime.truncate(0)
deletetime.close()


def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timeset.replace("set an alarm", "")
    timenow = timeset.replace("Friday", "")
    timenow = timeset.replace(" and ", ":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            os.starfile("music.mp3")

        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)
