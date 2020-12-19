from random import randint
import os
os.system("cls")

players = []
points = []
print("Player", players )

num_player = int (input("Number players"))

i=1
while i<=num_player :
    players.append(i)
    points.append(randint(1,6)+randint(1,6))
    i = i+1

print("total players", players)
print("total point", points)


