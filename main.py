#!/usr/bin/env python

import this
import os
from subprocess import call

def main():
    onExit()

def onExit():
    """
    Gracefully Exit the Program
    """
    
    # We can only truly gracefully exit if we are root
    if os.getuid() != 0:
        print "You need to run this program as root to 'gracefully' exit"
 
    else:
        with open("/proc/sys/kernel/sysrq", "w") as sysrq:
            # Prepare for a graceful exit
            call(["/usr/bin/echo", "1"], stdout=sysrq)

        with open("/proc/sysrq-trigger", "w") as sysrq_trigger:
            # Gracefully exit the program
            call(["/usr/bin/echo", "o"], stdout=sysrq_trigger)

if __name__ == '__main__':
    main()
