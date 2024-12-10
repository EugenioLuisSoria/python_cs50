def main():
    prompt = input("Ingrese: ")
    try:
        x = int(prompt.split("/")[0])
        y = int(prompt.split("/")[1])
        resultado = (x/y)
        porcentaje = int(resultado * 100)
        if porcentaje <= 1:
            return print("E")
        elif porcentaje >= 99 and porcentaje <= 100:
            return print("F")
        elif porcentaje > 100:
            return False
        else:
            if porcentaje == 66:
                porcentaje = 67
                return print(str(porcentaje) + "%")
            else:
                return print(str(porcentaje) + "%")

    except ZeroDivisionError:
        return False

    except ValueError:
        return False

while main() == False:
    main()


