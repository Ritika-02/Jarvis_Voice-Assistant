from body.speak import Speak
from body.listen import Listen


def MainExe():
    Speak('Main Execution......')

    while True:

        query = Listen()

        if 'hello' in query:
            Speak('Hi ! I am Jarvis!')

        elif 'bye' in query:
            Speak('Ok, Bye.')

MainExe()