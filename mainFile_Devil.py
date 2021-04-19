import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess
import time

pos=input("Enter Your Name: ")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak(hour)
    if hour>=0 and hour<12:
        speak("Good Morning! "+pos+"")

    elif hour>=12 and hour<18:
        speak("Good Afternoon "+pos+"")
    
    else:
        speak("Good Evening "+pos+"")
    speak("I'm Devil how may i help you")

def takeCommand():
    #it take microphone input from user and convert it into string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")  

    except Exception as e:
        print(e)
        print("Say That Again Please..")
        return "None"
    return query  
  
if __name__ == "__main__":   
    wishMe()

    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia..")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'open Google' in query:
            webbrowser.open("google.com")

        elif 'open twitter' in query:
            webbrowser.open('twitter.com')

        elif 'open Facebook' in query:
            webbrowser.open('fb.com')

        elif 'open' in query:
            speak("opening..")
            result = webbrowser.open(query)

        elif 'spotify' in query:
            subprocess.Popen('C:\\Users\\hp\\AppData\\Roaming\\Spotify\\Spotify.exe')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir The Time Is {strTime}")
            
        elif 'quit devil' in query:
            speak("Ohhk Have A Good Day")
            exit()