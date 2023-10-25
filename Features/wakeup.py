import speech_recognition as sr
import os


def Listen():

    r =sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source,0,3)      # listening mode 8 second...


    try:
        print('Recognizing....')
        query = r.recognize_google(audio,language ='en')

    except:
        return ""
    
    query = str(query).lower()
    print(query)
    return query



def WakeupDetected():
    query = Listen().lower()

    if 'wake up' in query:
        os.startfile(r'E:\Projects\Jarvis\main.py')
    else:
        pass

while True:
    WakeupDetected()