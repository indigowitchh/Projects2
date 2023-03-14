import random
def monster(biome):
    num = random.randrange(0,100)
    if biome == "hallway":
        if num < 20:
            print("A creature approaches quickly at you.")
        elif num < 50: #30 percent chance
            print("A tall figure peers from around the corner. He has no face.")
        elif num < 90:
            print("A clown doll sits in the corner of the room. Watching your every move.")
        else:
            print("A tall black figure walks towards you with open arms, but for some reason you feel like you can trust him.")
      
    elif biome == "bedroom":
        if num < 20:
            print("A creature approaches quickly at you.")
        elif num < 50: #30 percent chance
            print("A tall figure peers from around the corner. He has no face.")
        elif num < 90:
            print("A clown doll sits in the corner of the room. Watching your every move.")
        else:
            print("A tall black figure walks towards you with open arms, but for some reason you feel like you can trust him.")
     
    elif biome == "room?":
        if num < 25:
            print("A creature approaches quickly at you.")
        elif num < 75: #30 percent chance
            print("A tall figure peers from around the corner. He has no face.")
        elif num < 85:
            print("A clown doll sits in the corner of the room. Watching your every move.")
        else:
            print("A tall black figure walks towards you with open arms, but for some reason you feel like you can trust him.")
     
    elif biome == "different":
        if num < 20:
            print("A creature approaches quickly at you.")
        elif num < 50: #30 percent chance
            print("A tall figure peers from around the corner. He has no face.")
        elif num < 90:
            print("A clown doll sits in the corner of the room. Watching your every move.")
        else:
            print("A tall black figure walks towards you with open arms, but for some reason you feel like you can trust him.")
print("You wake up in your room. But, something feels off. Everything is the same as when you layed down and nothing is out of place. Except, it's quiet. No sound of family talking or the dogs walking around. Crap, you can't even hear the birds chirping. Curious, you decide to explore.")
room = 1
while True:
    if room == 1:
        print("You are in your bedroom, you can go (e)ast to leave the room.")
        monster("bedroom")
        choice = input()
        if choice == 'e' or choice == 'E'or choice == 'east':
            room = 2
        else:
            print("Sorry, not an option!")
    if room == 2:
        print("You are in the hallway. Or what you remember as the hallway. But, theres another door right in front of yours. You can go (w)est to go back to your room or (s)outh to explore the other door!")
        monster("hallway")
        choice = input()
        if choice == 'w' or choice == 'W'or choice == 'west':
            room = 1
        elif choice == 's' or choice == 'S'or choice == 'south':
            room = 3
        else:
            print("Sorry, not an option!")
    if room == 3:
        print("You are in your room again? Its a different room, yet everything is the same as your bedroom. Are you in a loop? However, instead of feeling alone, the feeling of being watched appears. You should leave immediately! You can go (n)orth back to what you think is the hallway, or (s)outh to another door!")
        monster("room?")
        choice = input()
        if choice == 'n' or choice == 'N'or choice == 'north':
            room = 2
        elif choice == 's' or choice == 'S'or choice == 'south':
            room = 4
        else:
            print("Sorry, not an option!")
    if room == 4:
        print("You are in a different room. One you do not recognize. That feeling of being watched only worsens. Yet, there's no door to lead you away. You're cornered! The only way back is to your supposed bedroom. You can go (n)orth")
        monster("different")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 3
        else:
            print("Sorry, not an option!")
