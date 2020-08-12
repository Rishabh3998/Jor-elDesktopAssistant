import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
# engine.say("I will speak for you")
# engine.runAndWait()
voices = engine.getProperty('voices')
# print(voices)
# print(voices[0].id)
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <18:
        Speak("Good Morning Sir")

    elif hour >= 12 and hour <18:
        Speak("Good Afternoon Sir")

    else:
        Speak("Good Evening Sir")

    Speak(" I am jor-el an advance AI , What can i do for you ")

def takeCommand():
    #it uses microphone to take the input from user 
    r = sr.Recognizer() 
    with sr.Microphone() as source  :
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio , language = 'en-in')
        print(f'user said : {query}\n')

    except Exception as e:
        print("Not Recognized please say it again")
        return "NONE"
    return query
    
def sendEmail(to , content):
    server = smtplib.SMTP('Emailid',587)
    server.ehlo()
    server.starttls()
    server.login('email','pass')
    server.sendmail('email', to , content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'Wikipedia' in query:
            Speak('Searching Wiki.......')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query , sentences = 2)
            Speak("According to wiki")
            print(results)
            Speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'Stack overflow ' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'path'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")

            print(f"Sir, the time is {strTime}")    
            Speak(f"Sir, the time is {strTime}")
            
        elif'open code' in query:
            codepath = "path"
            os.startfile(codepath)
        elif 'email to me ' in query:
            try:
                Speak("What should i say ??")
                content = takeCommand()
                to = "email"
                sendEmail(to , content)
                Speak("Email is sent")
            except exception as e:
                print(e)
                print("Sorry sir, Email is not sent")
                Speak("Sorry sir, Email is not sent")
        elif 'bye' or 'quit' in query:
            # if 'no' in query:

            print("bye sir have a good day!!!")
            Speak("bye sir have a good day!!!")
            exit()
        