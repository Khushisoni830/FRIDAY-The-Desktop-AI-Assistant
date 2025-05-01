import json
import requests
import pyttsx3

# Initialize the text-to-speech engine with the correct driver
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    """Speak out the given audio string."""
    engine.say(audio)
    engine.runAndWait()


def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=bcf72b5223094ba9b59d7729ce1083e8",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=bcf72b5223094ba9b59d7729ce1083e8",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=bcf72b5223094ba9b59d7729ce1083e8",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=bcf72b5223094ba9b59d7729ce1083e8",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=bcf72b5223094ba9b59d7729ce1083e8",
    }

    url = None
    speak("Which field news do you want? Options are: [business], [health], [science], [entertainment], [technology].")
    field = input("Type the field of news you want to hear: ").lower()

    # Find the URL for the requested field
    for key, value in api_dict.items():
        if key in field:
            url = value
            print("URL was found:", url)
            break

    if not url:
        speak("Sorry, the requested field was not found.")
        print("URL not found. Please try again.")
        return

    # Fetch and process news
    response = requests.get(url)
    if response.status_code != 200:
        speak("Failed to fetch news. Please check your API key or internet connection.")
        print("Error: Unable to fetch news. HTTP Status Code:", response.status_code)
        return

    news = response.json()
    speak("Here is the first news.")

    articles = news.get("articles", [])
    if not articles:
        speak("No news articles were found.")
        print("No articles available.")
        return

    for article in articles:
        title = article.get("title", "No title available")
        news_url = article.get("url", "No URL available")

        print(title)
        speak(title)
        print(f"For more info, visit: {news_url}")

        a = input("[Press 1 to continue] or [Press 2 to stop]: ")
        if a == "2":
            break

    speak("That's all for now. Have a great day!")
