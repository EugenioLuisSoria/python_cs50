import os
import sys

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


os.system("clear")

total = 0
while True:
    try:
        prompt = input("Item: ")
        prompt = prompt.lower().strip().title()
        if prompt in menu:
            total += menu.get(prompt)   #suma el precio al total  .get(prompt) => es el precio
            print(f"${total:.2f}")
        else:
            pass
    except EOFError:
        print("\n")
        break
    except:
        continue
