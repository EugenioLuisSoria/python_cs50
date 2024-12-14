def main():
    prompt = input("Ingrese: ")
    print(convert(prompt))

def is_int (string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def convert(fraction):
    try:
        x = int(fraction.split("/")[0])
        y = int(fraction.split("/")[1])
        resultado = (x/y)
        porcentaje = int(resultado * 100)
        return porcentaje

    except ValueError:
        return False




def gauge(percentage):
    if percentage < 1:
        return "E"
    elif percentage > 99:
        return "F"
    else:
        return f"{percentage}"

if __name__ == "__main__":
    main()
