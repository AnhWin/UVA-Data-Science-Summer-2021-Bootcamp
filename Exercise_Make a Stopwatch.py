# -*- coding: utf-8 -*-
"""
Created on Thu May 13 14:32:07 2021

@author: Situa
"""
#Prompt: Write a program that prints out the time it takes to run the program.

#invoke time module
import time

#set start time
stime = time.time()

#set end time
etime = time.time()

#time in between start and end
tlapsed = etime - stime

#display
print(tlapsed, "seconds")



