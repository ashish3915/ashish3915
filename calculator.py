def add(a,b):
    return a+b

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


print("Enter Your Choice")
print("0. Exit\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

while True:
    choice=int(input("Enter Choice (0,1,2,3,4):"))
    
    if choice==0:
        exit()

    if (choice==1 or choice==2 or choice==3 or choice==4):
        a=float(input("Enter first Number:"))
        b=float(input("Enter Second Number:"))

        if choice==1:
            print(a,"+",b,"=",add(a,b))

        if choice==2:
            print(a,"-",b,"=",sub(a,b))

        if choice==3:
            print(a,"*",b,"=",mul(a,b))

        if choice==4:
            print(a,"/",b,"=",div(a,b))
    else:
        print("Invalid Input.")
        exit()
