import os
os.system("clear")


def separator(a):
    new_list = [caracter for caracter in a]
    return new_list

def is_int (string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def main():
    os.system("clear")
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    while True:
        flagNumberFirst = False
        
        plate = plate.upper().strip().replace(" ", "-")
        while len(plate) > 6 or len(plate) < 2:
            return False
        plate_as_list = separator(plate)    
        new_to_calificate = []
        for caracter in plate_as_list:
            if is_int(caracter):
                new_to_calificate.append(int(caracter))
            else:
                new_to_calificate.append(caracter)
        
        i = len(new_to_calificate)-1
        valid_caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        #primeros dos caracteres LETRAS
        if is_int(new_to_calificate[0]) or is_int(new_to_calificate[1]):
            return False
        for caracter in new_to_calificate:
            #no numeros antes de letras    
            if flagNumberFirst == True and is_int(caracter) == False:
                print("caca1")
                return False            
            #caracter que NO SEA SIMBOLO O ESPACIO
            elif (is_int(caracter) == False) and (caracter not in valid_caracteres):
                print("caca2")
                return False
            #que el primer numero que aparezca no sea 0
            elif is_int(caracter) and caracter != 0 :
                flagNumberFirst = True
            elif flagNumberFirst == False and caracter == 0:
                print("caca3")                
                return False            
        else:
            return True
        
        
main()             
