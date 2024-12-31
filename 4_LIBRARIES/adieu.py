import os
import inflect
os.system("clear")
p =  inflect.engine()

frase_primera = "Adieu, adieu, to "
lista_nombres = []

while True:
    try:
        nombre = input("Insert name to say bye!: ")
    except EOFError:
        print("\n", end="")
        break
    lista_nombres.append(nombre)

if len(lista_nombres) != 1:
    for i in range(len(lista_nombres) -1):
        frase_primera = frase_primera + lista_nombres[i] + ", "
    frase_primera = frase_primera + "and " + lista_nombres[-1]
    print(frase_primera)
else:
    frase_primera = frase_primera + lista_nombres[0]
    print(frase_primera)
    
    
    
    
    
    
    
    
    




    
