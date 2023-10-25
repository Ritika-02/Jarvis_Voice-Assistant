#from httpx import QueryParams
import speech_recognition as sr
from googletrans import Translator

def Listen():
    r =sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source,0,4)      # listening mode 8 second...


    try:
        print('Recognizing....')
        query = r.recognize_google(audio,language ='en')

    except:
        return ""
    
    query = str(query).lower()
    return query

#Listen()

def Translation(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}")
    return data

#Translation(' कैसे हो ')

#Translation('how are you')

def micConnect():
    query = Listen()
    data = Translation(query)
    return data

micConnect()