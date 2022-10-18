
def add(a,b):
    return a + b 

def sub(a,b):
    return a - b 

def mul(a,b):
    return a * b

def div(a,b):
    return a/b

print("select opertation")
print("1 add ")
print("2 subtract ")
print("3 multipy ")
print("divide")
 
while True:
    choice = input("select one option ")
    if choice in ( '1', '2' ,'3' ,'4', "add", " subtract","multiply", "divide"):
        num1= input( " enter first digit ")
        num2= input(" enter second number ")
        if choice == '1' or "add":
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2' or "subtract":
           print(num1, "-", num2, "=", sub(num1, num2)) 
        elif choice == '3' or "multiply":
            print(num1, "x", num2, "=", mul(num1, num2))
        elif choice == '4' or "divide":
            print(num1, "/", num2, "=", div(num1, num2))
        next_calculation = input("lets do another calculation ?(yes/no): ")
        if next_calculation == "no":
            break
    else: 
        print("invalid option")

        