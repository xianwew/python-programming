import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setwarnings(False)                                   #turn the warnings off
GPIO.setmode(GPIO.BOARD)                                  #set the rppi connnector numbering mode
#initialize output, point out the port number for outputs and initalize them as low
GPIO.setup(29,GPIO.OUT, initial=GPIO.LOW)                  
GPIO.setup(31,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(32,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(33,GPIO.OUT, initial=GPIO.LOW)
#initialize input, indicate that when the switch is off, the value is 1(True)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_UP)


#define a function so I can call it recursively
def go():
    initial = 1                                          #create a value initial and assign it to 1
    while (initial == 1):                                #infinite loop
        ON = GPIO.input(13)                              #get the value from port 13, assign to 0 if pressed
        START = GPIO.input(15)                           #get the value from port 15, assign to 0 if pressed
        if(ON == False and START == False):              #if they are pressed simultaneouly, the if statement will go on
            start = 1                                    #define a valuable called start and get ready for the next loop
            speed = 0.45                                 #define the initial speed for blinking
            TS = time.time()                             #start counting time
            TE = TS                                      #define TE for timer
            while (start == 1 and TE - TS < 8):          #while start == 1 or TE - TS < 8, goes on
                Faster = GPIO.input(22)                  #get the value from port 22, assgin to 0 if pressed
                Slower = GPIO.input(12)                  #get the value from port 12, assgin to 0 if pressed
                if(Faster == False and speed > 0.1):     #if port 22 is pressed and speed > 0.1 (the speed can't less than 0), the speed can be increased
                    speed = speed - 0.2                  #decrease the time
                if(Slower == False):                     #if port 12 is pressed, the speed can be decreased
                    speed = speed + 0.2                  #increase the time
                #turn on each led by setting each port to high
                GPIO.output(29,GPIO.HIGH)
                GPIO.output(31,GPIO.HIGH)
                GPIO.output(32,GPIO.HIGH)
                GPIO.output(33,GPIO.HIGH)
                #turn on for a while
                sleep(speed)
                #turn off each led by setting each port to low
                GPIO.output(29,GPIO.LOW)
                GPIO.output(31,GPIO.LOW)
                GPIO.output(32,GPIO.LOW)
                GPIO.output(33,GPIO.LOW)
                #turn off for a while
                sleep(speed)
                #detect if the port 13 and port 15 are pressed, if pressed, assign OFF/END to 0.
                OFF = GPIO.input(13)
                END = GPIO.input(15)
                TE = time.time()                        #record time here
                if(OFF == False and END == False):      #if they are both pressed simultaneously, goes on   
                      #get out of the inner while loop by initializing the value
                      start = 0                         
                      ON = 1
                      START = 1
                      sleep(3)
                      go()                              #call the function recursively
                      
                

go()                                                    #call the function for the first time