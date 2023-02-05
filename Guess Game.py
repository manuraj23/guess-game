x=input("starting value: ")
y=input("Ending value: ")
z=input("No. of chances you want to give: ")
if x.isnumeric() and y.isnumeric() and z.isnumeric():
    x=int(x)
    y=int(y)
    z=int(z)
    if x<y and z>=1:
        import random
        a = random.randint(x,y)
        for i in range(1, z + 1):
            b= int(input("Enter your choice: "))
            i = i + 1
            if a == b:
                print("you won the game")
                break
            else:
                if i != z+1:
                    print("Try Again,",z-i+1,"chances remaining")
                elif i==z+1:
                    print("Chances Over")
            if i == z + 1:
                print("You lose the game")
                print("The number was", a)
    else:
        print("Invalid range")
else:
    print("Enter Integer value only")
