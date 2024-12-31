import sys
from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()   
    if len(sys.argv) == 1:
        prompt = input("Ingrese texto: ")
        fonts = figlet.getFonts()
        font = random.choice(fonts)
        figlet.setFont(font=font)
        return print(figlet.renderText(prompt))
        
    elif len(sys.argv) == 2:
        sys.exit("Parámetros erroneos")
        
    elif len(sys.argv) == 3 and (sys.argv[1] in ["-f", "--font"]):
        try:
            figlet.setFont(font=sys.argv[2])
            prompt = input("Ingrese texto: ")
            return print(figlet.renderText(prompt))
        except:
            sys.exit("Parámetros erroneos")
    else:
        sys.exit("Parámetros erroneos")
        
                
            
            
main()