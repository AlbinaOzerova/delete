shopping_list = input("Is milk on the list: ").lower()

print(shopping_list)

if "milk" in shopping_list:
    print("Milk is on the shopping list")
else:
    print("Milk is missing")