user_prompt = input("Ingrese calculo: ")

a, b, c = user_prompt.split()


a = int(a)
c = int(c)

match b:
    case "+":
        result = a + c
    case "-":
        result = a - c
    case "*":
        result = a * c
    case "/":
        result = a / c


print(f"{result:.1f}")
