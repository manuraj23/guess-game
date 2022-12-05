#project
x=int(input("Starting Value: "))
y=int(input("Ending Value: "))
if y-x>0:
    import random

    num1 = random.randint(x, y)
    # print(num1)
    a = int(input("Enter your choice: "))
    if a == num1:
        print("You win the game")
    else:
        print("Try Again")
        print("2 more chance left")
        b = int(input("Enter your choice: "))
        if b == num1:
            print("You win the game")
        else:
            print("Try Again")
            print("1 more chance left")
            c = int(input("Enter your choice: "))
            if c == num1:
                print("You win the game")
            else:
                print("You Lose")
                print("Number was: ", num1)
else:
    print("Invalid Range")