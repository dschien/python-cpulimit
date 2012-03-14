#!/usr/bin/python -O
'''
Created on 13 Aug 2011

@author: schien
'''
import os
import signal
import subprocess
import time
import argparse
import shlex
import sys

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('pid', metavar='pid', help='a pid to set cpu limits to in steps of 10%')

args = parser.parse_args()

cmd_stub = 'cpulimit -v -l {0} -p '

print sys.argv[1]

pro = None
for x in range(10, 110, 10):    
    print 'Press Enter to run at {0}% of load'.format(x)
    raw_input()
    if pro is not None :
        pro.terminate()    
    
    cmd = shlex.split(cmd_stub.format(x) + args.pid)    
    pro = subprocess.Popen(cmd)
    
print 'Press Enter to finish'
pro.terminate()
raw_input()

print 'done. exiting'
