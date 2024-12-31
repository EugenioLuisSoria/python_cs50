lista_para_pruebas = ["a","b","c", "d"]
tupla_para_constantes = [1,2,3,4]
diccionario = {
    "a" : 1 ,
    "b" : 2
}

a = dict(zip(tupla_para_constantes, lista_para_pruebas))


print(**a)
