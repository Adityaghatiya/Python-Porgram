#Function global declaration
x="Aditya"

def myfun():
    global x
    x="Adi"
    print(x)
myfun()
print(x)
