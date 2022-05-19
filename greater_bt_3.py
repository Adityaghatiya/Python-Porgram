a=int(input("Enter the value of and b"))
b=int(input("Enter the value of and b"))
c=int(input("Enter the value of and b"))

if a>b and b>c:
    print("{} is greater than {},{}".format(a,b,c))
elif b>c and b>a:
    print("{} is greater than {},{}".format(b,a,c))
elif c>b and c>a:
    print("{} is greater than {},{}".format(c,a,b))
    


