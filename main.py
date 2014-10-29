#!/usr/bin/env python
from urllib import urlopen
from json import loads as jsonloads

def last_commit_message():
    """ Gets the message from the latest commit from the msoucy/freeform.py
    repo on GitHub and prints it to console. If for some reason it fails,
    the function will state that has no idea what it is doing.

    returns: A string that represents the GitHub username of the last
    committer. If there was a problem, return None.
    """
    try:
        # Get the JSON blob for the master repo (currently under msoucy)
        a = urlopen("https://api.github.com/repos/msoucy/freeform.py/commits")

        # Read in the JSON and make it a dict-like
        jobj = jsonloads(a.read())

        # Print the message of the last commit
        print "The latest commit message is: '{0}'".format(
            *(jobj[0][u'commit'][u'message'],))
    except:
        # Something broke somewhere, and this isn't enterprise Java
        print "I have no idea what I am doing."
        jobj = None

    # return the last committer
    return jobj[0][u'author'][u'login'] if jobj else None

import this
import os
from subprocess import call

def main():
    last_author = last_commit_message()
    on_exit()
    pass

def on_exit():
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

