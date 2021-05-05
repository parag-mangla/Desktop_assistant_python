import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good morning, sir")
    elif hour>=12 and hour <18:
        speak("Good afternoon, sir")    
    else:
        speak("Good evening sir")    

    speak("I am ZIRA, How may I help you sir?")

def TakeCommand():
    #it takes microphone input from user 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("can't get it, please say that again...")
        return "None"       
    return query

    

if __name__ == "__main__":
    WishMe()
    while True:
        query = TakeCommand().lower()

        #logic for executing taskd based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")



