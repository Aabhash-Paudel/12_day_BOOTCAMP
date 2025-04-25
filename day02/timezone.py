import os
from time import sleep

micro = 0
sec = 0
min = 0
hrs = 0

while True:
    micro += 1
    if micro > 100:
        sec += 1
        micro = 0
    if sec > 60:
        min += 1
        sec = 0
    if hrs > 60:
        hrs += 1
        min = 0
    print(f"{hrs}: {min}: {sec}.{micro}")
    sleep(0.001)
    os.system("clear")
