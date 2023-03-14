import time #bring in files of prewritten code
import random

#function definitions ---------------------------------------------------------
def TimeKeygame():
    count = 0 #declaring and initializing variables
    tooSlow = False
    while count <5 and tooSlow == False: #gameloop
        num = random.randrange(0,10) #random number b/t 0-9
        TimeStart = time.perf_counter() #start a timer
        print("Press the number", num)
        userNum = int(input())
        TimeEnd = time.perf_counter()
        if TimeEnd-TimeStart <2 and userNum == num:
            print("Good job!")
            count+=1
        else:
            if userNum!=num:
                print("Wrong number!")
            else:
                print("Too slow!")
                tooSlow = True
            
    if tooSlow == True:
        print("You failed the task...")
        return False
    elif tooSlow == False:
        print("You completed the task!!!")
        return True
#end function definitions------------------------------------------------------
TimeKeygame()
