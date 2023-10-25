'''#from body.listen import Listen
from body.speak import Speak
from Features.clap import Tester

def Main():
    Tester()
    Speak('Jai Jinendra')

if __name__ =='__main__':
    Main()
'''


from Features.clap import Tester

data = Tester()
if 'True-Mic' == data:
    from Jarvis import MainExe
    MainExe()

'''def Listen():

    r =sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source,0,8)      # listening mode 8 second...


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
        MainExe()
    else:
        pass


while True:
    WakeupDetected() 

'''