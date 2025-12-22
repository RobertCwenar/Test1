#exercise 6.py
# Create a dictionary with sweet words and their prices. 
# If the dictionary is a sweet word you write a information that the words is in the dictionary.


candies = {}
print("Welcome to the sweets dictionary!")

while True:
    choose =input("Write add/display/sum/rename ('end' if you want to stop): ").strip().lower()
    if choose == "add":
        while True:
            candy = input("Write candy name: ").strip().capitalize()
            price = round(float(input("Write candy price (PLN): ")), 2)
            candies[candy] = price
            print(f"Added new candy '{candy}' with price {price} PLN.")
            
            answer = input("Do you want to add another? (y/n): ").strip().lower()
            if answer == 'n':
                break

    elif choose == "end":
        print("Exiting program.")
        break

    elif choose == "display":
        if candies:
            print("Display candies in the dictionary:")
            for candy, price in candies.items():
                print(f"{candy}: {price} PLN")
        else:
            print("The dictionary does not contain any data.")
        continue

    elif choose == "sum":
        sum_price=sum(candies.values())
        print(f"The total price of all candies is: {sum_price} PLN")
        continue
    elif choose == "rename":
        candy = input("Write candy name to rename: ").strip().capitalize()
        if candy in candies:
            new_candy = input("Write new candy name: ").strip().capitalize()
            candies[new_candy] = candies.pop(candy)
            print(f"Renamed candy '{candy}' to '{new_candy}'.")
        else:
            print(f"Candy '{candy}' is not in the dictionary.")
        continue

print("Final candies in the dictionary:")
for candy, price in candies.items():
    print(f"{candy}: {price} PLN")
