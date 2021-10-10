import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import wikipedia
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning!')
    elif 12 <= hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak("I am Tokiyo. I am here to help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        print("sry cant hear you...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prathameshshrikhande23667@gmail.com', 'password')
    server.sendmail('prathameshshrikhande23667@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to prathmesh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "prathameshshrikhande23667@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry prathamesh . I am not able to send this email")