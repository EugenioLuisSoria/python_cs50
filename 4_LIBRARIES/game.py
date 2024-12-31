import os
import random
os.system("clear")

user_level = -1
    
while user_level <= 0:
    try:
        user_level = int(input("Level? : "))
    except:
        continue
        

number = random.randint(1, user_level)
while True:
    
    user_guess = -1
    while user_guess < 0:
        try:
            user_guess = int(input("Guess? : "))
        except:
            continue
        
    if user_guess < number:
        print("Too small!")
        continue
    elif user_guess > number:
        print("Too large!")
        continue
    else:   
        print("Just right!")
        break    
    