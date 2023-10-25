import pyttsx3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By          #By : used for targeting
from time import sleep

#windows based : 
# offline too
# less voices
'''def Speak(Text):
    engine = pyttsx3.init('sapi5')
    #sapi5 : windows API which helps us to take voice

    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)

    engine.setProperty('rate',170)
    # rate : speed , normal speed : 170

    print("")
    print(f'You : {Text}.')
    print("")
    engine.say(Text)
    engine.runAndWait()

#Speak('Hello Sir')
'''

#Chrome Based : 
# -clear and more voices
# -word limit 


chrome_options = Options()
chrome_options.add_argument('--log-level=3')    # Avoids overprintind due to selenium
chrome_options.headless = True    
Path = 'Database\chromedriver.exe'
chrome_service = webdriver.chrome.service.Service(Path)
driver = webdriver.Chrome(service = chrome_service, options =chrome_options)
driver.maximize_window()

#website opens
website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)

#selection of voice type
ButtonSelection = Select(driver.find_element(by = By.XPATH, value ='//*[@id="sprachwahl"]'))
ButtonSelection.select_by_visible_text('British English / Brian')


def Speak(Text):
    lengthofText = len(str(Text))

    if lengthofText ==0:
        pass
    else:
        print('')
        print(f"AI : {Text}.")
        print('')
        data = str(Text)
        xpathofsec ='//*[@id="voicetext"]'
        driver.find_element(By.XPATH, value =xpathofsec).send_keys(data)   # Data is send
        driver.find_element(By.XPATH, value ='/html/body/div[3]/div[2]/form/input[1]').click()
        driver.find_element(By.XPATH, value='//*[@id="voicetext"]').clear()

        if lengthofText >= 30:
            sleep(4)

        elif lengthofText >=40:
            sleep(6)
        
        elif lengthofText >=50:
            sleep(8)

        elif lengthofText >= 70:
            sleep(10)

        elif lengthofText >= 100:
            sleep(12)
        
        else:
            sleep(2)

#Speak()