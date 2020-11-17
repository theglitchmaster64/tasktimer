#!/usr/bin/python

import os, time, sys
from threading import Thread
import matplotlib.pyplot as plotter
import numpy as np

STOP_THIS = False
TASK_LOG = {}
TOTAL_TIME = 0

def timer(countdown):
    global STOP_THIS
    global TASK_LOG
    global TOTAL_TIME
    secs = countdown
    task_no = 0
    while True:
        if STOP_THIS == True:
            task_no +=1
            task_time = countdown - secs
            TASK_LOG[task_no] = task_time
            print('task {} time:  '.format(task_no)+str(task_time))
            TOTAL_TIME += task_time
            print('total time:   '+str(TOTAL_TIME)+'\n')
            secs = countdown
            STOP_THIS = False
        time.sleep(1)
        secs -=1
        if secs == 0:
            os.system('play -nq -t alsa synth 0.25 sine 880')

def stop():
    x=input()
    global STOP_THIS
    global TASK_LOG
    if x != 'q':
        STOP_THIS = True
    elif x == 'q':
        print('generating report...')
        fig = plotter.figure(figsize=(16,9))
        tno = list(TASK_LOG.keys())
        ttime = list(TASK_LOG.values())
        plotter.bar(tno,ttime)
        plotter.savefig('stats.png')
        print('done! report saved to stats.png')
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
