import pyttsx3

class Greeting:
    def __init__(self , logger , response):
        self.logger = logger
        self.response = response

    engine = pyttsx3.init('sapi5')
    
    voices = engine.getProperty('voices')
    
    engine.setProperty('voice',voices[0].id)
    
    @staticmethod
    def Speak(response):
        engine.say(response)
        engine.runAndWait()
