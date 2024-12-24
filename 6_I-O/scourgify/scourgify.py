import sys, csv

def invertir_nombre(last_first):
    last, first = map(str.strip, last_first.split(","))
    return first, last


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
    with open(sys.argv[1], newline='') as before, open("after.csv", "w") as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
        writer.writeheader()
        #rows_cvs = []
        for row in reader:
            first, last = invertir_nombre(row['name'])
            house = row['house']
            writer.writerow(
                {
                    "first" : first,
                    "last" : last,
                    "house" : house
                }
            )


    

            
        
        

