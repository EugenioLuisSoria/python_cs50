def main():
    prompt_hour = input("Ingrese hora actual: ")
    hora_convertida = convert(prompt_hour)
    if  7 <= hora_convertida <= 8:
        print("breakfast time") 
    if  12 <= hora_convertida <= 13:
        print("lunch time") 
    if  18 <= hora_convertida <= 19:
        print("dinner time") 
    

def convert(time):
    horas, minutos = time.split(":")
    horas = float(horas)
    minutos = float(minutos)
    minutos /= 60
    hora_convertida = horas + minutos
    return hora_convertida
   


if __name__ == "__main__":
    main()
    
