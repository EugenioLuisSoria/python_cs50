import sys, csv

def invertir_nombre(apellido_nombre):
    nombre, apellido = map(str.strip, apellido_nombre.split(","))
    return f"{nombre}, {apellido}"


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    f, e = sys.argv[1].split(".")
except:
    sys.exit("Not a valid file")

if e != "csv":    
    sys.exit("Not a CSV file")
    
else:
    with open(sys.argv[1]) as file:
        for row in file:
            row[0] =
        
        

