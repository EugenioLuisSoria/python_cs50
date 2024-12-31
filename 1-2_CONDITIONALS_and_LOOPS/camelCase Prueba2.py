def main():
    string = input("Ingrese nombre archivo: ")
    new_string = ""
    
    for letra in string:
        if letra.isupper():
            new_string += f"_{letra}"
        else:
            new_string += letra
    print(f""" 
          {string}
          
          {new_string}
          
          """)

    
        
main()