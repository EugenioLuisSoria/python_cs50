def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 10
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


def main():
    user_greating = input("Saludame!: ")
    print(value(user_greating))

if __name__ == "__main__":
    main()
