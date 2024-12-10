import emoji


def main():
    frase = input("Ingrese frase: ")
    print(emoji.emojize(frase, language='alias'))


main()
