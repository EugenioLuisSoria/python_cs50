import os

os.system("clear")
 
def main():
    string = input("Ingrese su nombre de archivo: ")
    new_string = ""

    for letra in string:
        if letra.isupper():
            nueva_letra = letra.lower()
            new_string += f"_{nueva_letra}"
        else:
            new_string += letra

    print(f"Su viejo nombre: {string}")
    print(f"Su nuevo nombre: {new_string}")

main()
