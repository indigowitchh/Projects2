friends = ("jesse", "googy", "rick", "cynthia", "daniela", "jenessa") #tuple!

ages = [] #list

print(friends)

ages.append(int(input("enter age for friend 1:")))
ages.append(int(input("enter age for friend 2:")))
ages.append(int(input("enter age for friend 3:")))
ages.append(int(input("enter age for friend 4:")))
ages.append(int(input("enter age for friend 5:")))
ages.append(int(input("enter age for friend 6:")))

print(friends[0],":", ages[0])
print(friends[1],":", ages[1])
print(friends[2],":", ages[2])
print(friends[3],":", ages[3])
print(friends[4],":", ages[4])
print(friends[5],":", ages[5])   

#find average of numbers
sum = 0
for i in ages:
    sum+= i
    
average = sum/(len(ages))
print("The average age is", average)
