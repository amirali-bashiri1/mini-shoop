import os

from dotenv import load_dotenv
from products import products


load_dotenv()
admin_password = os.getenv("QUIZ_ADMIN_PASWORD")
open_admin = input(" do you want to open admin mode? yes/no : ")
if open_admin == "yes":
    enterd_password = input("enter admin password : ")

    if enterd_password == admin_password:
        print("admin! hi...")
    else:
        print("wrong password")


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
