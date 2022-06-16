import pyttsx3

class Speaker:
    def __init__(self, voice_id = "german", voice_rate = 200, voice_volume = 1):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', voice_rate)
        self.engine.setProperty('voice', voice_id)
        self.engine.setProperty('volume', voice_volume)
        self.currentTask = None

    def changeRate(self, voice_rate):
        return engine.setProperty('rate', voice_rate)
    def speak(self, line):
        if self.engine.isBusy():
            print("BUSYY!!!")
            #self.currentTask.cancel()
        self.engine.say(line)
        self.engine.runAndWait()