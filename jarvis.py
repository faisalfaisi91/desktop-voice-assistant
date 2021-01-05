import pyttsx3
import speech_recognition as sr  # pip3 install speechRecognition
import datetime
import wikipedia  # pip3 install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[16].id)
engine.setProperty('voice', voices[16].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I'm Jarvis Sir, what I can do for you?")


def takeCommand():
    # It takes microphone input from the users and returns string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print("User said: ", query)

    except Exception as e:
        print(e)

        print("Say that again please")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("faisal.supple@gmail.com", "bcsblaster")
    server.sendmail("faisal.supple@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic  for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open netflix' in query:
            webbrowser.open('netflix.com')
        elif 'open amazon' in query:
            webbrowser.open('amazon.com')
        elif 'play music' in query:
            music_dir = '/home/faisal/Music'
            songs = os.listdir(music_dir)
            print(songs)
            # os.startfile(os.path.join(music_dir, songs[0]))
            os.system(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is:")
            print(strTime)
            speak(strTime)
        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "faisal.supple@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry for the inconvenice, I can't sent email at this time")
        elif 'quit' in query:
            speak("Thank you sir, we will talk again soon")
            exit()
