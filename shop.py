inventory = [' ', ' ', ' ']
items = ["Potions $5", "Food $3", "Keys $10"]
Dabloons = 20

def money(Dabloons):
    leave = False
    while leave == False and Dabloons != 0:
        print("Hello traveler, welcome to the shop, you have", Dabloons, "dabloons")
        print("Your inventory:", inventory, ". Shop items:", items)
        choice= input("Press p to purchase a potion, f for food, k for key, and q to leave the shop")
        
        if choice == 'p' and Dabloons >=5:
            print("You purchased a potion!")
            inventory[0] = "Potion"
            Dabloons -= 5
            print("You have", Dabloons, " dabloons remaining")
            print("---------------------------------------------------------------")
        
        elif choice == 'f' and Dabloons >=3:
            print("You purchased food!")
            inventory[1] = "Food"
            Dabloons -=3
            print("You have", Dabloons, "dabloons remaining")
            print("---------------------------------------------------------------")
        
        elif choice =='k' and Dabloons >=10:
            print("You purchased a key!")
            inventory[2] = "Key"
            Dabloons -= 10
            print("You have", Dabloons, "dabloons remaining")
            print("---------------------------------------------------------------")
        
        elif choice =='q':
            print("Goodbye traveler, have a safe journey!")
            leave = True
            print("---------------------------------------------------------------")
        
        else:
            print("Sorry, not an option")
            print("---------------------------------------------------------------")
            
money(Dabloons)
