import os
os.system("clear")

lista = {}
while True:
    try:
        prompt = input("")
        prompt = str(prompt.upper().strip())
        if prompt in lista:
            lista[prompt] += 1
        else:
            lista[prompt] = 1
        continue
    except EOFError:
        break
    except:
        continue

lista_ordenada = dict(sorted(lista.items()))
print(lista_ordenada)


for item in lista_ordenada:
    print(lista_ordenada[item], item)
    
    
    #IMPORTANTISIMO:
    #el item ==> es la clave
    #el lista_ordenada[item] ==> es el valor
    
    
    