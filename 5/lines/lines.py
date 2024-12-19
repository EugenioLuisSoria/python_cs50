import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    f, e = sys.argv[1].split(".")
except:
    sys.exit("Not a Python file")

if e == "py":    
    counter = 0
    with open(sys.argv[1]) as file:
        for row in file:
            row = row.strip()
            if len(row) == 0:
                continue
            else:    
                if row[0] == "#":
                    continue
                else:
                    counter +=1
    print(counter)
                    
    
else:
    sys.exit("Not a Python file")
