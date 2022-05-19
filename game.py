#Stone paper scisor....
#Players of Match
#Here x=Aditya
#y=viveek
x=input("Aditya Bata ky bola")
y=input("Viveek Bata ky bola")

#Eqipment
a="stone"
b="paper"
c="scissor"
#Condition 1: Rock beats paper
if(x==a and y==b):
    print(" Paper win")
    print("Congratulation Viveek")
elif(x==a and y==c):
    print(" Stone Beats scissor ")
    print("Contratulation Aditya")
elif(x==b and y==c):
    print("Scissor cuts paper")
    print("Congrats Viveek")
elif(x==b and y==a):
    print("Aditya win")
elif(x==c and y==a):
    print("Viveek Win the game")
elif(x==c and y==b):
    print("congrats Aditya")
elif(x==a  and y==a):
    print("Koi ni jeeta")

elif(x==b  and y==b):
    print("Koi ni jeeta")

elif(x==c  and y==c):
    print("Koi ni jeeta")
    
    
    


    

    
