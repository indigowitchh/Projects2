import random

#-------------------------------------------------------------------------------------
def BattleSystem(monsterType, playerHealth):
    if monsterType == "Creeper":
        monsterHealth = 20
        print("A creeper attacks!")
    elif monsterType == "Skeleton":
        monsterHealth = 40
        print("A skeleton attacks!")
    elif monsterType == "Enderdragon":
        monsterHealth = 200
        print("An enderdragon attacks!")
    elif monsterType == "Pillager":
        monsterHealth = 25
        print("A pillager attacks!")
        
    while monsterHealth>0 and playerHealth>0:
        if monsterType == "Creeper":
            monsterAttack = random.randrange(20,31)
        elif monsterType == "Skeleton":
            monsterAttack = random.randrange(10,16)
        elif monsterType == "Enderdragon":
            monsterAttack = random.randrange(40,81)
        elif monsterType == "Pillager":
            monsterAttack = random.randrange(25, 36)
        
        
        print("The", monsterType, "attacks for", monsterAttack)
        playerHealth= playerHealth-monsterAttack
        print("Your health is now", playerHealth)
        
        playerAttack = random.randrange(25,35)
        print("You attack for", playerAttack)
        monsterHealth = monsterHealth-playerAttack
        print("The monsters health is now", monsterHealth)
        
    if monsterHealth<0:
        print("You slained the monster!")
    else:
        print("You are defeated by the monster...")
    return playerHealth
#-------------------------------------------------------------------------------------
rando=random.randrange(0,100)

if rando <= 25:
    BattleSystem("Skeleton", 100)
elif rando <= 50 and rando > 25:
    BattleSystem("Creeper", 100)
elif rando <=75 and rando >50:
    BattleSystem("Enderdragon", 100)
elif rando <= 100 and rando > 75:
    BattleSystem("Pillager", 100)
