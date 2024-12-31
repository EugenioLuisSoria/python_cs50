

import sys
from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()
    prompt = input("Ingrese texto: ")

    if len(sys.argv) > 1 and sys.argv[1] in ["-f", "--font"]:
        if len(sys.argv) > 2:
            try:
                figlet.setFont(font=sys.argv[2])
            except:
                sys.exit("caca")
        else:
            print("Debe especificar una fuente")
            return

    print(figlet.renderText(prompt))

if __name__ == "__main__":
    main()