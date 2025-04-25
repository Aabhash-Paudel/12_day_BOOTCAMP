import os
from time import sleep

h,m,s = 0,0,0
while True:
    print(f"{h:02}:{m:02}:{s:02}")
    sleep(0.00000001)
    s += 1
    os.system("clear")
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h== 12:
        h = 0
        m = 0
        s = 0
