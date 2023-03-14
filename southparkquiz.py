kenny = 0
cartman = 0
kyle = 0
stan = 0

choice = input("What is your favorite color? (g)reen, (o)range, (b)lue, or (r)ed")
if choice == 'g':
  kyle = kyle + 1
elif choice == 'o':
  kenny = kenny + 1
elif choice == 'b':
  stan = stan + 1
elif choice == 'r':
  cartman = cartman + 1
else:
  print("Sorry not an option!")

choice = input("How would your friends describe you? (q)uiet, (e)vil, (c)aring, or (d)epressed")
if choice == 'c':
  kyle = kyle + 1
elif choice == 'q':
  kenny = kenny + 2
elif choice == 'd':
  stan = stan + 1
elif choice == 'e':
  cartman = cartman + 2
else:
  print("Sorry, not an option!")

choice = input("Whats your weakness? (p)oor, (f)atherless, (h)ated, or (y)oungest")
if choice == 'h':
  kyle = kyle + 1
elif choice == 'p':
  kenny = kenny + 1
elif choice == 'y':
  stan = stan + 1
elif choice == 'f':
  cartman = cartman + 2
else:
  print("Sorry, not an option!")

choice = input("What is your hobby? (w)atching tv, (p)laying w/ friends, (s)leeping, or (r)elaxing")
if choice == 'p':
  kyle = kyle + 2
elif choice == 'r':
  kenny = kenny + 2
elif choice == 's':
  stan = stan + 2
elif choice == 'w':
  cartman = cartman + 1
else:
  print("Sorry, not an option!")

choice = input("What is your favorite animal? (d)og, (c)at, (o)rca, or (n)one of the above")
if choice == 'o':
  kyle = kyle + 1
elif choice == 'n':
  kenny = kenny + 1
elif choice == 'd':
  stan = stan + 1
elif choice == 'c':
  cartman = cartman + 1
else:
  print("Sorry, not an option!")
  
choice = input("Whats your favorite food? (e)verything, (n)othing, (b)agels, or (h)emp")
if choice == 'b':
  kyle = kyle + 1
elif choice == 'n':
  kenny = kenny + 1
elif choice == 'h':
  stan = stan + 1
elif choice == 'e':
  cartman = cartman + 1
else:
  print("Sorry, not an option!")

choice = input("What are you known for? (d)ying, (c)rying, (s)inging, or (m)anipulation")
if choice == 's':
  kyle = kyle + 2
elif choice == 'd':
  kenny = kenny + 2
elif choice == 'c':
  stan = stan + 2
elif choice == 'm':
  cartman = cartman + 2
else:
  print("Sorry, not an option!")

if kenny >= cartman and kenny >= kyle and kenny >= stan:
  print("You are Kenny!")
elif cartman >= kyle and cartman >= stan:
  print("You are Cartman!")
elif kyle >= stan:
  print("You are Kyle!")
else:
  print("You are Stan!")
