#Prompt: Write a program that prints out the time it takes to run the program.

#set start time
stime <- proc.time()

#code to do something
print('hello word')

#set end time
etime <- proc.time()

#time that elapsed
tlapsed <- etime - stime

#display
print(tlapsed)