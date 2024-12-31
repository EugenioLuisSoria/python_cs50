fruits = "apple avocado banana cantaloupe grapefruits grapes honeydew-melon kiwifruit lemon lime nectarine orange peach pear pineapple plums strawberries sweet-cherries tangerine watermelon"
calories = "130 50 110 50 60 90 50 90 15 20 60 80 60 100 50 70 50 100 50 80 "

f = fruits.split(" ")
c = calories.split(" ")

dictionary = dict(zip(f, c))

prompt = input("fruta: ").replace(" ", "-").lower()

if prompt in dictionary:
    print(f"Calories: {dictionary[prompt]}")
else:
    print("")