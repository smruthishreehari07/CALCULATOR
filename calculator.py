import time
print("Welcome to the calculator")
time.sleep(2)
e=input("To continue press c or to exit press q ")
if e=="c":
    p=input("What is your name? ")
    print(f"Hi {p} ")
    try:
        a=int(input("Enter the first number: "))
        b=int(input('Enter the second number: '))
        o=input(f"Enter the operation you wanna perform: ")
        match o:
            case "+":
                print("Addition is", a+b)
            case "-":
                print("Difference is", a-b)
            case "*":
                print("Multiplication is", a*b)
            case "/":
                print("Division is", a/b)
            case "%":
                print("Modulus is", a%b)
    except Exception as e:
        print(f" {p} its not valid,",e)
    print("Thankyou ")   
else:
    exit()   

