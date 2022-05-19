x=int(input("Enter the require year"))
print("x=",x)

if(x%400==0 and x%100==0):
    print("{} is leap year".format(x))

elif(x%4==0 and x%100!=0):
    print("{} is leap year".format(x))
else:
    print("{} is not a leap year".format(x))

#Loop program

for i in range(10):
    print(i)

for i in range(3,8):
    print(i)

for i in range(1,2,11):
    print(i)
