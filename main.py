from products import products


name = input("Whats your name? ")

print("Welcome to Mini Shop")

print("Products:")

for item in products:
    print(item["name"], "-", item["price"], "$")


product_name = input("Which product do you want? ")

price = 0

for item in products:
    if product_name.lower() == item["name"].lower():
        price = item["price"]
        break


if price != 0:
    print("Price:", price, "$")

    file = open("purchases.txt", "a")
    file.write(f"{name} - {product_name} - {price}$\n")
    file.close()

    print("Purchase saved")

else:
    print("Product not found")
