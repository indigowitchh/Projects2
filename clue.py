import random

#lists
students = ['Jesse', 'Lukas', 'Ricardo', 'Simon', 'Jackie', 'Dom', 'Rey', 'Sayid', 'Alan', 'Keven']
locations = ['room 110', 'the gender-neutral bathroom', 'the cafeteria', 'the main office', 'the  future center']

  
#function
def Clue():
    #variables
    num = random.randrange(0,100)
    numVictim = random.randrange(0,10)
    numSuspect = random.randrange(0,10)
    numPlace = random.randrange(0,5)
    victim = students[numVictim]
    suspect = students[numSuspect]
    place = locations[numPlace]
    
    if num < 10:
        print (victim, "got water ballooned in", place, "by", suspect)
    elif num < 30:
        print(victim, "got pied in the face in", place, "by", suspect)
    elif num < 65:
        print(victim, "got choco chip cookies that actually were raisin in", place,"by", suspect)
    elif num < 80:
        print(victim, "got their shoelaces tied together and tripped in", place,"by", suspect)
    else:
        print(victim, "got turned into a bunny with a tranfiguration raygun in", place,"by", suspect)
   
#function calls   
quit = False
while quit == False:
    choice = input("Press any key for a scenario, q to quit")
    if choice != 'q':
        Clue()
    else:
        print("Thanks for playing!")
        quit = True 
