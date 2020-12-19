import os
from random import randint, uniform 
os.system("cls")


def rand_integer() :
    nz = randint(1,6)
    return nz

acumulado1 = 0
dice1 = 0
dice2 = 0

print("Enter first number: ")
print("[1]. Basic Level ")
print("[2]. Medium Level ")
print("[3]. Advance Level")
print("Please, enter any option (1-3): ")
op = input()
if op == '1' :
    print("Basic Level 50 Points")
    print("::::::::::::::::::::::::")
    
    players = []
    suma = []

    print("Player", players )

    num_player = int (input("Number players"))
        

    for i in range(1, num_player+1):
       acumulado = 0
       suma.append(dice1+dice2)
    i=0    
    j =1

    while suma[i] <=50:
        print("Digite enter para volver a lanzar dados", i+1)
        input("")
        dice1 = rand_integer()
        dice2 = rand_integer()
        

        while j<=num_player :
            players.append(j)
            suma[i]= suma[i]+dice1+dice2
            j = j+1
            

        print("total players", players)
        suma[i]= suma[i]+dice1+dice2

       
        print("acumulado", suma)    

              
               
      
elif op == '2' :
    print("Basic Level 70 Points")
    print("::::::::::::::::::::::::")
    while acumulado1 <= 70 or acumulado2 <= 70:
        
        print("Turno jugador1")
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        print("Dice1->",dice1,"Dice2->",dice2)
        print ("Lleva", acumulado1,"+",dice1,"+",dice2)
        acumulado1 = acumulado1+dice1+dice2 
        print("Acumulado del jugador1:", acumulado1 )
        print("____________________________:")
        print("Turno jugador2")
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        print("Dice 1->",dice1,"Dice 2->",dice2)
        print ("Lleva", acumulado2,"+",dice1,"+",dice2)
        acumulado2 = acumulado2+dice1+dice2
        print("Acumulado del jugador2:", acumulado2 )
        print("____________________________:")
    

        if acumulado1 >=70 :
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Ganador jugador1")
               
        elif acumulado2 >=700:
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Ganador jugador2")    
               
elif op == '3' :
    print("Basic Level 100 Points")
    print("::::::::::::::::::::::::")
    while acumulado1 <= 100 or acumulado2 <= 100:
        
        print("Turno jugador1")
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        print("Dice1->",dice1,"Dice2->",dice2)
        print ("Lleva", acumulado1,"+",dice1,"+",dice2)
        acumulado1 = acumulado1+dice1+dice2 
        print("Acumulado del jugador1:", acumulado1 )
        print("____________________________:")
        print("Turno jugador2")
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        print("Dice 1->",dice1,"Dice 2->",dice2)
        print ("Lleva", acumulado2,"+",dice1,"+",dice2)
        acumulado2 = acumulado2+dice1+dice2
        print("Acumulado del jugador2:", acumulado2 )
        print("____________________________:")
    

        if acumulado1 >=100 :
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Ganador jugador1")
               
        elif acumulado2 >=100:
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Ganador jugador2")    
               
else :
    print("::: Invalid option :::")