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
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    while True:
        plate = plate.upper().strip().replace(" ", "-")
        while len(plate) < 2:
            return False
        return True

if __name__ == "__main__":
    main()
