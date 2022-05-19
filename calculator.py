#Printing Calculator.........................

number_1=input("Enter the first number")
number_2=input("Enter the second number")

#function for addition
def addition(a,b):
    return(a+b)

#function for subtraction
def subtration(a,b):
    return(a-b)

#function for multiplication
def mul(a,b):
    return(a*b)

#function for divide
def div(a,b):
    if(b==0):
        print("Division is not posible in this as second number is zero")
    else:
        return(a/b) 
#function for power
def pow(a,b):
    if(b==0):
        print("Power  by zero is not posible")
    else:
        return(a**b)

print("---------------------------------------------")
print("Enter the required datatypes...")

