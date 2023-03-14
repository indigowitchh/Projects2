#THE BACKROOMS by Rey 12/2022

import winsound #used for beeps
import random #module for random generator
import os #module for colors

inventory = ['phone','empty','empty', 'empty', 'empty'] #player inventory

#GameOver Function-------------------------------------------------------------------------------------------
def falldown():
    num = random.randrange(0,100)
    if inventory[2]=="lucky charm": #lucky charm in inventory raises chances of winning by ALOT
        if num < 5: #5 percent chance
            print("You trip over your own foot. As you fall onto the floor, the ground beneath you dissapears. You're in the sky now, watching yourself get closer and closer to earths surface. You plummet to your death.")
            return 1
        elif num < 85: #80 percent chance
            print("The light gets brighter. You run towards it and it blinds you. You close your eyes and when you open them again you wake up in your room. You can hear your family, the birds chirping and your dog barking! It was just a dream.")
            return 2
        else: #15 percent chance
            print("You twist your ankle. Now you have a limp. You must continue on with your journey.")
            return 3
    else:
        if num < 50: #50 percent chance 
            print("You trip over your own foot. As you fall onto the floor, the ground beneath you dissapears. You're in the sky now, watching yourself get closer and closer to earths surface. You plummet to your death.")
            return 1
        elif num < 70: #20 percent chance
            print("The light gets brighter. You run towards it and it blinds you. You close your eyes and when you open them again you wake up in your room. You can hear your family, the birds chirping and your dog barking! It was just a dream.")
            return 2
        else: #30 percent chance 
            print("You twist your ankle. Now you have a limp. You must continue on with your journey.")
            return 3

#Monster Function-------------------------------------------------------------------------------------------
def monster(biome):
    num = random.randrange(0,100)
    if biome == "hallway":
        if num < 20: #20 percent chance
            print("A creature scurries past you.")
        elif num < 50: #30 percent chance
            print("A tall figure peers from around the corner. He has no face.")
        elif num < 90: #40 percent chance
            print("A clown doll sits in the corner of the room. Watching your every move.")
        else: #10 percent chance
            print("A tall black figure walks towards you with open arms, but for some reason you feel like you can trust him.")
     
    elif biome == "room?":
        if num < 25: #25 percent chance
            print("A creature scurries past you.")
        elif num < 75: #50 percent chance
            print("A tall figure peers from around the corner. He has no face.")
        elif num < 85: #10 percent chance 
            print("A clown doll sits in the corner of the room. Watching your every move.")
        else: #15 percent chance
            print("A tall black figure walks towards you with open arms, but for some reason you feel like you can trust him.")
     
    elif biome == "different":
        if num < 20: #20 percent chance 
            print("A creature scurries past you.")
        elif num < 50: #30 percent chance
            print("A tall figure peers from around the corner. He has no face.")
        elif num < 90: #40 percent chance
            print("A clown doll sits in the corner of the room. Watching your every move.")
        else: #10 percent chance
            print("A tall black figure walks towards you with open arms, but for some reason you feel like you can trust him.")

#Variables------------------------------------------------------
room = 1
doExit = False
dead = False

#Rooms------------------------------------------------------------------------------------------------------
print("You wake up in your room. But, something feels off. Everything is the same as when you layed down and nothing is out of place. Except, it's quiet. No sound of family talking or the dogs walking around. Crap, you can't even hear the birds chirping. Curious, you decide to explore with your phone in your pocket.")

while doExit == False:
    if room == 1: #room/starting point
        print("You are in your bedroom, you can go (e)ast to enter the hallway, (n)orth to enter your closet, or (s)outh to go into the bathroom.")
        print("Your inventory is", inventory)
        choice = input()
        if choice == 'e' or choice == 'E'or choice == 'east':
            room = 4
        elif choice == 'n' or choice == 'N' or choice == 'north':
            room = 2
        elif choice == 's' or choice == 'S' or choice == 'south':
            room = 3
        else:
            print("Sorry, not an option!")
            
    if room == 2: #closet
        print("You open the closet door. It is pitch black. Even if you flash your phone's flashlight, nothing appears. It is just dark. You don't want to enter, so you put your hand in. It just dissapears. You can go (s)outh to go back to your bedroom")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south':
            room = 1
        else:
            print("Sorry not an option!")
            
    if room == 3: #bathroom
        print("You swing your bathroom door open. To your surprise, it is completely trashed, almost like a tornado hit it. As you walk through the bathroom and check the mirror, your reflection smiles back at you. Even though you are not smiling. The drawer below you is open but you're hesitant to check. You can go (n)orth.")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 1
        elif choice == "drawer" or choice == "d":
            winsound.Beep(500,500)
            print("The item you grab shines in your hand. It feels lucky. You put it in your pocket.")
            inventory[2] = "lucky charm" #adding to inventory
            print("Your inventory updated! Your inventory is now", inventory) #tell player their inventory
        else:
            print("Sorry not an option!")
            
    if room == 4: #hallway
        print("You are in the hallway. Or what you remember as the hallway. But, there still is no sound... You are alone. You can go (w)est to go back to your room, (n)orth into your baby siblings room, (s)outh to enter the random door you've never seen before, or (e)ast to go to your living room!")
        monster("hallway")
        choice = input()
        if choice == 'w' or choice == 'W'or choice == 'west':
            room = 1
        elif choice == 's' or choice == 'S'or choice == 'south':
            room = 6
        elif choice == 'n' or choice == 'N' or choice == 'north':
            room = 5
        elif choice == 'e' or choice == 'E' or choice == 'east':
            room = 8
        else:
            print("Sorry, not an option!")
            
    if room == 5: #baby room
        print("Although your house is silent and no one seems to be around, the sound of your baby sibling crying rings through your ears. Yet, they are no where to be found, the only thing left of them is their pacifer. The longer you spend in the room, the louder the crying gets. Save your eardrums and go (s)outh to enter the hallway!")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south':
            room = 4
        elif choice == 'p' or choice == 'P' or choice == 'pacifier' or choice == 'Pacifier':
            winsound.Beep(500,500)
            print("You grab the pacifier in the crib. You hold it tight along your journey.")
            inventory[3]= "pacifier" #adding to inventory
            print("Your inventory updated! Your inventory is now", inventory) #tell player their inventory
        else:
            print("Sorry, not an option!")
            
    if room == 6: #room copy
        print("You are in your room again? Its a different room, yet everything is the same as your bedroom. Are you in a loop? However, instead of feeling alone, the feeling of being watched appears. You should leave immediately! You can go (n)orth back to what you think is the hallway, or (s)outh to another door!")
        monster("room?")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 4
        elif choice == 's' or choice == 'S'or choice == 'south':
            room = 7
        else:
            print("Sorry, not an option!")
            
    if room == 7: #random room
        print("You are in a different room. One you do not recognize. A rug is convientaly placed in the middle of the room. That feeling of being watched creeps up on you. Yet, there's no door to lead you away. You're cornered! The only way back is to your supposed bedroom. You can go (n)orth")
        monster("different")
        choice = input()
        if choice == 'r' or choice == 'rug' or choice == 'Rug':
            winsound.Beep(500,500)
            print("You found a key!")
            inventory[1] = "key" #adding to inventory
            print("Your inventory updated! Your inventory is now", inventory) #tell player their inventory
        elif choice == 'n' or choice == 'N' or choice == 'north':
            room = 6
        else:
            print("Sorry, not an option!")
    
    if room == 8: #living room
        print("Huh.. the living room seems normal. Everything is in place, no sign of weird happenings. The only weird think is a random door to your left but its locked. Do you dare to explore? You can go (n)orth to enter the random door, (w)est back into the hallway, or (s)outh into your kitchen.")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north':
            key = False
            for i in range(len(inventory)):
                if inventory[1] == "key": #you need key to trigger win option
                    key = True
            if key == True:
                print("You open the door with the key.")
                room = 10
            else:
                print("The door is locked...") #when you don't have key
        elif choice == 's' or choice == 'S' or choice == 'south':
            room = 9
        elif choice == 'w' or choice == 'W' or choice == 'west':
            room = 4
        else:
            print("Sorry not an option")
            
    if room == 9: #kitchen
        print("Holy cow! The kitchen is covered in blood! It looks like a crazy crime scene with a singular sword in the middle of the room. Your stomach drops and you feel like throwing up. You need to leave. You weren't supposed to see this. Go (n)orth into the living room.")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 8
        elif choice == 'sword' or choice == 'Sword' or choice == 's' or choice == 'S':
            winsound.Beep(500,500)
            print("You pick up the sword and take it with you for protection. You feel tougher already.")
            inventory[4] = "sword" #adding to inventory
            print("Your inventory updated! Your inventory is now", inventory) #tell player their inventory
        else:
            print("Sorry, not an option!")
            
    if room == 10: #second hallway/ending point
        print("Another hallway? However, theres no ending. Or so it seems. You walk down the hallway for what seems like forever. The door back to your living room gets smaller and smaller. You finally reach a dead end. The only way back to 'society' is to go (s)outh")
        choice = input()
        result = falldown() #code that has game end in 2 different ways
        if result == 1:
            doExit = True
            dead = True
        elif result == 2:
            doExit = True
        if choice == 's' or choice == 'S' or choice == 'south':
            room = 8
        else:
            print("Sorry, not an option!")

#Win/Lose Statements-------------------------------
if dead == True: #game over result
    os.system('color 4') #color change
    winsound.Beep(200,600)
    print("You lose. Better luck next time. You died with", inventory) #final inventory
    print("___/|")
    print("\o.O| Meow! Game over!")
    print("(___)")

elif dead != True: #winning result
    os.system('color 2') #color change
    winsound.Beep(900,900)
    print("You won! Congrats! You survived with", inventory)#final inventory
    print("___/|")
    print("\o.O| Meow! Good job!")
    print("(___)")
