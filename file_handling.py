"""Writing a python script to write the execution time for a variable in a file when the variable is used to
  find factorial using iteration and recursion method"""

f=open("myfirstfile.txt","w")
x="Jai  Shree Ram"
y="Jai Sanidev"
f.write(x)
f.write("\n")
f.write(y)

for x in f:
    print(x)
f.close()
