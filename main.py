from kettler import Kettler
from speaker import Speaker
import time

speaker = Speaker()
serial = Kettler()
serial.connect()
prevRes = Kettler.getStatus()[4]

# dummy code
def buttonPressed():
    return False

while True:
    status = Kettler.getStatus()
    # Check for changed resistance
    # If so, output new resistance, and return the script to restart
    if prevRes != status[4]:
        speaker.say('Watt ' + status[4])
        prevRes = status[4]
        return True
    if buttonPressed():
        line = ""
        if status[0] != 0:
            line += "Puls " + status[0] + "."
        line += status[2] + "kmh."
        line += status[3] * 100 + "Kilometer gelaufen." 
        speaker.speak(line)
    time.sleep(0.5)

"""engine = pyttsx3.init()
engine.setProperty('voice', 'german')
engine.say("400 km h")
engine.runAndWait()
"""
"""
Puls 0
Kmh 2
RPM 1
Watt 4 WIEVIEL WIDERSTAND
Kj 5
time 6
Strecke 3 100stel Kilometer
"""