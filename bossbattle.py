import random

inventory = ['phone','potion','empty', 'sock', 'empty']
PlayerHealth = 100 #set player health

#Monster Battle------
def Battle(PlayerHealth): #battle function
    MonsterHealth = 50 #set monster health
    while MonsterHealth >0 and PlayerHealth>0: #mini game loop, quits game when you or monster dies
        #you attack the monster
        if inventory[2]== "lucky charm":
            damage = random.randrange(20,31) #more damage with lucky charm
        else:
            damage = random.randrange(5,11)
        print("You hit the monster for", damage, "HP.")
        MonsterHealth -= damage
        #monster attacks you
        damage = random.randrange(5,16)
        print("The monster bites you for", damage, "HP.")
        PlayerHealth -= damage
        #pause
        print("You have", PlayerHealth, "HP left, and the monster has", MonsterHealth, "HP left.")
        choice = input("Press p for potion, f to feed, any other key to keep fighting")
        if choice == 'p':
            if inventory[1]=="potion":
                print("Glug glug (xp+20)")
                PlayerHealth +=20
                inventory[1] == "empty"
            else:
                print("Sorry, you have no potion")
        if choice == 'f':
            if inventory[3] == "sock":
                print("You feed the dragon a dirty sock, it is happy and goes away!")
                MonsterHealth = 0
            else:
                print("You tried to feed it, but dont have a sock, it is upset that you don't have a sock so it eats you in one bite!")
                PlayerHealth = 0
        print()
    if PlayerHealth <=0:
        print("You were defeated and lost the game!")
    else:
        print("You defeated the monster and won!")
    return PlayerHealth

#variables----
room = 1
doExit = False
#Rooms------------------------------------------------------------------------------------------------------
print("You wake up in your room. But, something feels off. Everything is the same as when you layed down and nothing is out of place. Except, it's quiet. No sound of family talking or the dogs walking around. Crap, you can't even hear the birds chirping. Curious, you decide to explore.")

while doExit == False and PlayerHealth>0:
    if room == 1:
        print("You are in your bedroom, you can go (n)orth to enter your closet, or (s)outh to go into the bathroom.")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 2
        elif choice == 's' or choice == 'S' or choice == 'south':
            room = 3
        else:
            print("Sorry, not an option!")
            
    if room == 2:
        print("You open the closet door. It is pitch black. Even if you flash your phone's flashlight, nothing appears. It is just dark. You don't want to enter, so you put your hand in. It just dissapears. You can go (s)outh to go back to your bedroom")
        print("A monster attacks you!")
        PlayerHealth = Battle(PlayerHealth)
        
        break #ends game
        
    if room == 3:
        print("You swing your bathroom door open. To your surprise, it is completely trashed, almost like a tornado hit it. As you walk through the bathroom and check the mirror, your reflection smiles back at you. Even though you are not smiling. The drawer below you is open but you're hesitant to check. You can go (n)orth.")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 1
        elif choice == "drawer" or choice == "d":
            print("The item you grab shines in your hand. It feels lucky. You put it in your pocket.")
            inventory[2] = "lucky charm"
        else:
            print("Sorry not an option!")
