from products import products


name = input("Whats your name? ")

print("Welcome to Mini Shop")

print("Products:")

for item in products:
    print(item["name"], "-", item["price"], "$")


product = input("Which product do you want? ")

for item in products:
    if product.lower() == item["name"].lower():
        print("Price:", item["price"], "$")

        file = open("purchases.txt", "a")
        file.write(f"{name} - {item["name"]} - {item["price"]}$\n")
        file.close()

        print("Purchase saved")
        break
