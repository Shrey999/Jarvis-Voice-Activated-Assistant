import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else: 
        speak("Good Evening!")

    speak("I am Jarvis. How may i help you")            

def takeCommand():
    #this function take microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #time limit for user to take pause while speaking a phrase or sentence, by default it is 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")    

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "none"
    return query    

#this function will work only if we enable less secure apps in poour google admin console which is applicable only for organizational emails, hence this function will not work here
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login("youremail@gmail.com", "your-password")
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()


if __name__ == '__main__':
    wishMe()
    while True:
    # if 1:    
        query = takeCommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia",  "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")    
        
        elif 'open google' in query:
            webbrowser.open("google.com")    
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")    
      
        elif 'play music' in query:
            music_dir = "D:\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            r1 = random.randint(0, len(songs)-1 )
            os.startfile(os.path.join(music_dir, songs[r1]))
        
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}") 

        elif 'open vs code' in query:
            code_path = "C:\\Users\\shrey\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)    

        # elif 'send email' in query:
        #     try:
        #         speak("What should i say?")
        #         content = takeCommand()
        #         to = "youremail@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry, I am not able to send this email")
        
        elif 'quit' in query:
            exit()

