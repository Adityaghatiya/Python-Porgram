#prime number code using python
a=int(input("Enter the required number"))
print("Thus the required number is "+ str(a))

if(a==0):
    print("It is zero number")
    for i in range(2,a-1):
       if(a%i==0):
          print("It is not prime number")

else:
    print("It is an prime number")
