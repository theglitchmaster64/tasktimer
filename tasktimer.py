#!/usr/bin/python

import os, time, sys
from threading import Thread

STOP_THIS = False

def timer(countdown):
    global STOP_THIS
    secs = countdown
    total_time = 0
    while True:
        if STOP_THIS == True:
            print('task time:  '+str(countdown - secs))
            total_time += countdown - secs
            print('total time: '+str(total_time))
            secs = countdown
            STOP_THIS = False
        time.sleep(1)
        secs -=1
        if secs == 0:
            os.system('play -nq -t alsa synth 0.25 sine 880')

def stop():
    x=input()
    global STOP_THIS
    if x == '':
        STOP_THIS = True
    elif x == 'q':
        sys.exit(0)

if __name__=='__main__':
    #get sysargs
    if len(sys.argv) == 1:
        print('enter countdown time in secs')
        sys.exit(1)
    else:
        try:
            countdown = int(sys.argv[1])
        except ValueError:
            print('invalid argument')
            sys.exit(1)
    #do stuff
    t1 = Thread(target=timer,args=(countdown,))
    t1.daemon = True
    t1.start()
    while True:
        stop()
