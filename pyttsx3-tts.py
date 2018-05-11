# pyttsx-3 TTS

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20) #set rate
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.50) #set volume
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #voice id 0
engine.say('The quick brown fox jumped over the lazy dog.')
engine.setProperty('voice', voices[10].id) #voice id 10
engine.say('The quick brown fox jumped over the lazy dog.')
engine.setProperty('voice', voices[5].id) #voice id 5
engine.say('The quick brown fox jumped over the lazy dog.')
new = []
new.append("Helllo")
new.append("World")
x = (" ").join(new)
engine.say(format(x))
engine.runAndWait()
engine.stop()
