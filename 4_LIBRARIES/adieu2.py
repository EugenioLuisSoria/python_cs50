import os
import inflect
os.system("clear")
p =  inflect.engine()


frase_primera = "Adieu, adieu, to "
lista_nombres = []

while True:
    try:
        nombre = input("Insert name to say bye!: ")
        lista_nombres.append(nombre)
    except EOFError:
        print()
        break

lista_final = p.join(lista_nombres)

print("Adieu, adieu, to " + lista_final)
    
    