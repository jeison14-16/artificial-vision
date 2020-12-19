
import os
os.system("cls")

def add_place(x):
    placas_list.append(x)
    print("placas actualizadas", placas_list)
    print("len", len(placas_list))

placas_list = [123, 'AXZ123']
fruits_list = ["APPLE","ORANGE",]
numbers_list = [1,2,3,'4']

print("Placas ", placas_list)
print("Len", len(placas_list))#show list lengt
print("Fruits", fruits_list)
print("Len", len(fruits_list))#show list lengt
print("Numbers", numbers_list)
print("Len", len(numbers_list))#show list lengt


for element in range (len(placas_list)):
    print(placas_list[element] )

#main
print(":::::::::::::")
placa = input("INgrese la placa del vehiculo")
add_place(placa)