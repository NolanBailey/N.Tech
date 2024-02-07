import time
from alive_progress import alive_bar
import string

def loading_text():
#(v.1)    print("Loading", end='\r')
#(v.1)    time.sleep(1)
#(v.1)    print("Loading.", end='\r')
#(v.1)    time.sleep(1)
#(v.1)    print("Loading..", end='\r')
#(v.1)    time.sleep(1)
#(v.1)    print("Loading...", end='\r')
#(v.1)    time.sleep(1)

    for x in 1000, 1500, 700, 0:
       with alive_bar(x) as bar:
           for i in range(1000):
               time.sleep(.005)
               bar()

print('©N. Tech')
time.sleep(2)
print('𝐇𝐀𝐋𝐋𝐎𝐖𝐄𝐄𝐍 𝔓𝔞𝔯𝔞𝔡𝔢')
time.sleep(0.5)
loading_text()
name = input('This is the legend of... ')
name = name.capitalize()
print("Once apon a time...")
time.sleep(1)
print(name + ' started a long sanding Halloween tradition...')
time.sleep(1)
print('But now it has gone all wrong...')
time.sleep(1)
print('Opening window...')
time.sleep(.5)
loading_text()
