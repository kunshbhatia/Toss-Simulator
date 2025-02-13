# Toss
name = input("Enter Your Name Please: ")

print()
print(f"Welcome {name} To Toss Simulator " . center(100) . upper())
print(" (Best of 3) " . center(100) . upper())
print()
a = "Enter H or T"
v = "H denotes Heads and T denotes Tails"
print(a . center (100))     
print(v . center(100))
print()
print(" Round I " . center(100) . upper())
b = str(input("Enter Your Choice: "))
import random
c = ["H", "T"]
d = random.choice(c)
if b == d:
    print("Correct , Score :- 1/3 ")
    print()
    print(" Round II " . center(100) . upper())

    b = str(input("Enter Your Choice: "))
    import random
    c = ["H", "T"]
    d = random.choice(c)

    if b == d:
            print("Correct , Score :- 2/3 ")
            print(" Round III " . center(100) . upper())

            b = str(input("Enter Your Choice: "))
            import random
            c = ["H", "T"]
            d = random.choice(c)

            if b == d:
                print("Correct , Score :- 3/3 ")
                print()
                print(" Congrats For Finishing The Game , made by Kunsh " . center(100) . upper())
                input("Press Enter to Exit")


            elif b != d:
                 print("Better Luck Next Time , score :- 2/3 ")
                 print()
                 input("Press Enter to Exit")
                 print()
                 quit()
                 
    elif b != d:
        print("Better Luck Next Time , score :- 1/3 ")
        print()
        input("Press Enter to Exit")
        print()
        quit()
 
elif b != d:
    print("Better Luck Next Time , score :- 0/3 ")
    print()
    input("Press Enter to Exit")
    print()
    quit()