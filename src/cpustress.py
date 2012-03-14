#!/usr/bin/python -O
'''
Created on 13 Aug 2011

@author: schien
'''
import os
import signal
import subprocess
import time

# The os.setsid() is passed in the argument preexec_fn so
# it's run after the fork() and before  exec() to run the shell.
cmd = 'bash -c "while : ; do true ; done"'
sleeptime = 10

print "About to execute " + cmd
pro = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                       shell=True, preexec_fn=os.setsid)
print 'sleeping for ' + str(sleeptime) + " seconds" 
#time.sleep(sleeptime)
#print 'done'
#os.killpg(pro.pid, signal.SIGTERM)  # Send the signal to all the process groups
