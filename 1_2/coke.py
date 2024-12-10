price = 50
amount = 0

while True:
    user_coin = int(input("Ingrese moneda: "))
    while user_coin != 25 and user_coin != 10 and user_coin != 5:
        print(f"Amount Due: {price}")
        user_coin = int(input("Ingrese moneda: "))
        
    
    price -= user_coin
    if price > 0:
        print(f"Amount Due: {price}")
    else:
        print(f"Change Owed: {price * (-1)}")
        break
        
        