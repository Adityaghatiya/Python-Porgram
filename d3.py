#Finding best of two  internal marks out of three internal
#************Internal calculation***************
m1=int(input("Enter the 1st internal marks"))
m2=int(input("Enter the 2st internal marks"))
m3=int(input("Enter the 3st internal marks"))

if(m1>m3 and m2>m3):
    tot=(m1+m2)
    print("Thus the required marks be m1 and m2",tot)

elif(m1>m2 and m3>m2):
    tot=(m1+m3)
    print("Thus the required marks be m1 and m3",tot)
elif(m2>m1 and m3>m1):
    tot=(m1+m3)
    print("Thus the required marks be m2 and m3",tot)
elif(m1==m2 and m1>m3):
    tot=(m1+m2)
    print("Thus the required marks be",tot)
elif(m1==m3 and m1>m2):
    tot=m1+m3
    print("Thus the required marks be")


