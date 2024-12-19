import sys, csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    f, e = sys.argv[1].split(".")
except:
    sys.exit("Not a Python file")

if e != "csv":    
    sys.exit("Not a CSV file")
    
else:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))
        
        
        

