def user_input():
    a=int(input("Enter the a"))
    b=int(input("Enter the b"))

    return(a,b)
def add(a,b):
    return (a+b)
a,b=user_input()
#add(a,b)
print(a,"+",b,"=",add(a,b))
