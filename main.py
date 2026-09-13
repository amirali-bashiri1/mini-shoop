
from products import products


name = input("Whats your name? ")

print("Welcome to Mini Shop")

print("Products:")

for item in products:
    print(item["name"], "-", item["price"], "$")


product = input("Which product do you want? ")
quantity = int(input("How many do you want? "))


for item in products:
    if product.lower() == item["name"].lower():
        total_price = item["price"] * quantity

        print("Total price:", total_price, "$")

        file = open("purchases.txt", "a")
        file.write(f"{name} - {item['name']} - {quantity} - {total_price}$\n")
        file.close()

        print("Purchase saved")
        break
