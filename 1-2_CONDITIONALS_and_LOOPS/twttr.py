import re
def main():
    user_prompt = input("Ingrese palabra: ")
    new_word = re.sub("[aeiouAEIOU]", "", user_prompt)
    print(f"Esta es su nueva palabra: {new_word}")
    
    

def main2():
    user_prompt = input("Ingrese palabra: ")
    vocals = "aeiouAEIOU"
    new_word = ""
    for letter in user_prompt:
        if letter not in vocals:
            new_word += letter
        else:
            new_word += ""
            
    return new_word
            
        
main2()  