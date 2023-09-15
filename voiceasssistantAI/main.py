import speech_recognition as sr
import pyttsx3
import webbrowser
import openai
import os
import datetime
from config import apikey


openai.api_key = apikey

def ai(message):
    text = f"OpenAI response for prompt: {message}\n************\n\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": message  
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    generated_text = response["choices"][0]["text"]
    print(generated_text)
    text += generated_text

    
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    
    with open(f"openai/{''.join(message.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    print(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            return "I couldn't understand. Please repeat."
        except sr.RequestError as e:
            return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Jarvis AI")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.org"],
                 ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir....")
                webbrowser.open(site[1])
        if "open music" in query.lower():
            musicPath = r"C:\Users\Mohit\Downloads\Music\downfall-21371.mp3"
            os.startfile(musicPath)

        if "show time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} hour and {min} minutes")

        if "open chrome" in query.lower():
            os.system(r'"C:\Program Files\Google\Chrome\Application\chrome.exe"')

        if "open brave" in query.lower():
            os.system(r'"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"')

        if "open vs code" in query.lower():
            os.system(r'"C:\Users\Mohit\AppData\Local\Programs\Microsoft VS Code\Code.exe"')

        if "using artificial intelligence".lower() in query.lower():
            ai(message=query)
