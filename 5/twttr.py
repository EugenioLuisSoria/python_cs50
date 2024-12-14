import pytest

def shorten(word):
    vocals = "aeiouAEIOU"
    new_word = ""
    for letter in word:
        if letter not in vocals:
            new_word += letter
        else:
            new_word += ""
            
    return new_word
            


def main():
    user_word = input("Introduzca palabra: ")
    print(shorten(user_word))

if __name__ == "__main__":
    main()