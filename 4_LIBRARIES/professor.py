import os
import random


def main():
    os.system("clear")
    level = get_level()
    respuestas_correctas = 0
    preguntas = 0

    while True:

        while preguntas != 10:
            fallos_seguidos = 0
            num1, num2 = generate_integer(level)
            while True:
                if fallos_seguidos == 3:
                    print(f"{num1} + {num2} = {num1 + num2}")
                    preguntas += 1
                    break
                try:
                    user_respuesta = int(input(f"{num1} + {num2} = "))
                    if num1 + num2 != user_respuesta:
                        fallos_seguidos += 1
                        print("EEE")
                        continue
                    elif num1 + num2 == user_respuesta:
                        respuestas_correctas += 1
                        preguntas += 1
                        break
                except:
                    continue
        break

    print(f"Score: {respuestas_correctas}")


def get_level():
    user_level = -1
    while user_level <= 0 or user_level > 3:
        try:
            user_level = int(input("Level? : "))
        except:
            continue
    return user_level


def generate_integer(level):
    match level:
        case 1:
            number1 = random.randint(0, 9)
            number2 = random.randint(0, 9)
        case 2:
            number1 = random.randint(10, 99)
            number2 = random.randint(10, 99)
        case 3:
            number1 = random.randint(100, 999)
            number2 = random.randint(100, 999)
        case _:
            raise ValueError

    return number1, number2


if __name__ == "__main__":
    main()
