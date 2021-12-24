# setup
lista = []

x = input(str("Dime tu palabra: "))

hazte = "Hazte un " + x
que = "Un que?"
un = "Un " + x

temp_string = ""

for i in range(1, 1000):
    for j in range(1,i + 1):
        temp_string += hazte + ";"
    for j in range(1,i + 1):
        temp_string += que + ";"
    for j in range(1,i + 1):
        temp_string += un + ";"

lista = temp_string.split(";")
lista.pop()

index = 0

flag = True # flag para ver si escribe o se compara

# print menu
print("Respuestas:\n-\tHazte un " + x + "\n-\tUn que?" + "\n-\tUn " + x + "\n\n\nEscribe la respuesta o 'exit' para parar el juego:\n")

# bucle del juego
while True:
    if flag == True:
        print(lista[index])
        index += 1
        flag = False
        continue
    
    temp = input(str())

    if temp == "exit":
        print("\nPues vete a la mierda")
        break
    
    if flag == False:
        if temp == lista[index]:
            index += 1
            flag = True
            continue
        else:
            print("\nPerdiste tonto")
            break
