#e-SpeakNG TTS

import os

os.system('espeak -a 150 -s 140 -p 65 -g 11  "What is two plus two?" -ven+f4')
ans = int(input())
if (ans == 4):
    os.system('espeak -a 150 -s 140 -p 65 -g 11  "correct answer" -ven+f4')
else:
    os.system('espeak -a 150 -s 140 -p 65 -g 11  "wrong answer" -ven+f4')
