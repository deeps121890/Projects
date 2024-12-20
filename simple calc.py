'''
def display_menu():
    print("\n-----Calculator Menu-----")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Divison")
    print("5.Exit")
    return input("Choose an operation (1-5):")
def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    if b==0:
        return "Erron:Divison by zero is undefined."
    return a/b
while True:
    choice=display_menu()
    if choice in["1","2","3","4"]:
        try:
            num1=float(input())
            num2=float(input())
            if choice=="1":
                result=add(num1,num2)
                print(f"Result:{num1}+{num2}={result}")
            elif choice=="2":
                result=subtract(num1,num2)
                print(f"Result:{num1}-{num2}={result}")
            elif choice=="3":
                result=multiply(num1,num2)
                print(f"Result:{num1}*{num2}={result}")
            elif choice=="4":
                result=divide(num1,num2)
                print(f"Result:{num1}/{num2}={result}")
        except ValueError:
            print("Invalid input! please enter numbers only.")
    elif choice=="5":
        print("exiting the calculator,Good bye!")
        break
    else:
        print("Invalid choice! please select a valid operation")
o/p:
-----Calculator Menu-----
1.Addition
2.Subtraction
3.Multiplication
4.Divison
5.Exit
Choose an operation (1-5):1
784
783
Result:784.0+783.0=1567.0

-----Calculator Menu-----
1.Addition
2.Subtraction
3.Multiplication
4.Divison
5.Exit
Choose an operation (1-5):2
87980
64783
Result:87980.0-64783.0=23197.0

-----Calculator Menu-----
1.Addition
2.Subtraction
3.Multiplication
4.Divison
5.Exit
Choose an operation (1-5):3
4837849
4783789
Result:4837849.0*4783789.0=23143248829861.0

-----Calculator Menu-----
1.Addition
2.Subtraction
3.Multiplication
4.Divison
5.Exit
Choose an operation (1-5):4
48792
5030
Result:48792.0/5030.0=9.700198807157058

-----Calculator Menu-----
1.Addition
2.Subtraction
3.Multiplication
4.Divison
5.Exit
Choose an operation (1-5):5
exiting the calculator,Good bye!

