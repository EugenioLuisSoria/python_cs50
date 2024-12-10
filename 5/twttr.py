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
    print(shorten())





if __name__ == "__main__":
    main()