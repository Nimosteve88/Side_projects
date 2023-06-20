import sys
from sys import exit
import time
import random
import sqlite3
import ChristmasDatabaseTask
from datetime import datetime


MENU_PROMPT = """-----Shoppin4Christmas Stock Management System-----
Please choose one of these options:
1) Add a new Product
2) See all Products
3) Find a Product by Name
4) Delete a Product by Name 
5) Customer Version
6) Exit

Your Selection: """

def customer_process():
    print("Here are the items that you can Purchase from:")
    products = ChristmasDatabaseTask.select_all_products()
    print("ProductTypeID: 1 - Christmas Meals   2 - Christmas Decorations   3- Christmas Electricals")

    print("Name  -------  Price  -------  Quantity  -------  ProductTypeID")

    for product in products:
        print(f"{product[1]}-------({product[2]})-------({product[3]})-------{product[4]}")

    chosenone = str(input("Enter the Product Name you would like to Purchase: "))
    choses = ChristmasDatabaseTask.select_product(chosenone)

    for chose in choses:
        print(f"{chose[1]}-------({chose[2]})-------({chose[3]})-------{chose[4]}")
        quantity = chose[3]
        quantity -= 1
        name = chose[1]
        price = chose[2]
        productTypeID = chose[4]
    now = datetime.now()
    currentDate = now.strftime("%d/%m/%Y ")
    currentTime = now.strftime("%H:%M")
    lastname = str(input("Enter Your Last Name again please for Verification"))
    if __name__ == "__main__":
        search = ChristmasDatabaseTask.customerid(lastname)
        newvers = search[0]
        with sqlite3.connect("Shoppin4Christmas.db") as db:
            cursor = db.cursor()
            cursor.execute(
                "insert into CustomerOrder (ProductName, Date, Time, CustomerID, PriceofProduct) values (?,?,?,?,?)",
                (name, currentDate, currentTime, newvers, price))
            db.commit
        productID = ChristmasDatabaseTask.select_productID(name)
        productID1 = productID[0]
        orderID = ChristmasDatabaseTask.select_orderID(newvers)
        orderID1 = orderID[0]
        values = (orderID1, productID1)
        ChristmasDatabaseTask.insert_orderItem(values)
    with sqlite3.connect("Shoppin4Christmas.db") as db:
        cursor = db.cursor()
        cursor.execute("delete from Product where Name=?",(name,))
        cursor.execute("insert into Product (Name, Price, Quantity, ProductTypeID) values (?,?,?,?)", (name, price, quantity, productTypeID))
        db.commit

    anotherchance = input("If you would like to add another Product to your order enter Y, if not Enter N")
    if anotherchance == 'Y' or anotherchance == 'y':
        customer_process()
    else:
        print("Your Order has been completed")
        time.sleep(2)
        menu()

def menu():
    connection = ChristmasDatabaseTask.connect()
    ChristmasDatabaseTask.create_product()

    while (user_input := input(MENU_PROMPT)) != "6":
        if user_input == "1":
            producttype = int(input("If it's a Christmas Meal enter 1, Christmas Decoration enter 2, Christmas Electrical enter 3"))
            name = str(input("Enter the Product name: "))
            price = float(input("Enter the Price"))
            quantity = int(input("Enter the quantity: "))
            result = (name, price, quantity, producttype)

            ChristmasDatabaseTask.insert_data(result)
            print("Your new product has now been added to the database")
        elif user_input == "2":
            products = ChristmasDatabaseTask.select_all_products()
            print("ProductTypeID: 1 - Christmas Meals   2 - Christmas Decorations   3- Christmas Electricals")
            print("Name  -------  Price  -------  Quantity  -------  ProductTypeID")
            for product in products:
                print(f"{product[1]}-------({product[2]})-------({product[3]})-------{product[4]}")
                quantity1 = product[3]
                if quantity1 <= 0:
                    with sqlite3.connect("Shoppin4Christmas.db") as db:
                        cursor = db.cursor()
                        cursor.execute("delete from Product")
                        db.commit
                    time.sleep(1)
                    print("An item has been removed as it ran out of Stock. Please wait for every single stock to refill.")
                    time.sleep(1.5)
                    ChristmasDatabaseTask.autorefill()
                    newproducts = ChristmasDatabaseTask.select_all_products()
                    print("The overall stock has now been updated")
                    print("ProductTypeID: 1 - Christmas Meals   2 - Christmas Decorations   3- Christmas Electricals")
                    print("Name  -------  Price  -------  Quantity  -------  ProductTypeID")
                    time.sleep(1.5)
                    for product in newproducts:
                        print(f"{product[1]}-------({product[2]})-------({product[3]})-------{product[4]}")

        elif user_input == "3":
            name = str(input("Enter the Product Name to find: "))
            products = ChristmasDatabaseTask.select_product(name)

            for product in products:
                print(f"{product[1]}-------({product[2]})-------({product[3]})-------{product[4]}")
        elif user_input == "4":
            name = str(input("Enter the Product Name you want to remove: "))
            ChristmasDatabaseTask.delete_product(name)

        elif user_input == "5":
            beenherebefore = input(
                "If you have already shopped here before then enter YES, If this is your very first time enter "
                "NO")
            if beenherebefore == 'YES' or beenherebefore == 'Yes' or beenherebefore == 'yes':
                lastname = str(input("Enter Your Last Name"))
                if __name__ == "__main__":
                    search = ChristmasDatabaseTask.customer(lastname)
                    newvers = search[0]
                    if lastname == newvers:
                        option = str(input(
                            "Would you like to see your Order History since you have shopped here before?, enter YES if you do, if not Enter No"))
                        if option == 'YES' or option == 'Yes' or option == 'yes' or option == 'Y':
                            id = ChristmasDatabaseTask.customerid(newvers)
                            history = id[0]
                            products = ChristmasDatabaseTask.orderHistory(history)
                            print("Here is your Order History")
                            time.sleep(2.5)
                            print("Name of Product  -------  Price  -------  Date  -------  Time  -------  CustomerID")
                            time.sleep(1.5)
                            for product in products:
                                print(
                                    f"{product[0]}-------({product[1]})-------({product[2]})-------{product[3]}-------{product[4]}")
                            time.sleep(3)
                            continued = str(
                                input("Would like to continue Shopping? Enter yes if would like to, no if you don't"))
                            if continued == 'Yes' or continued == 'YES' or continued == 'Y':
                                customer_process()
                            else:
                                print("Please leave")
                                menu()
                        else:
                            print("Okay, you will be directed to the Customer Process")
                            customer_process()
                    else:
                        while lastname == newvers:
                            lastname = str(input("Enter Your Last Name"))
                        customer_process()

            else:
                firstname = str(input("Enter Your First Name"))
                lastname = str(input("Enter Your Last Name"))
                street = str(input("Enter the Street you live in: "))
                town = str(input("Enter the Town you live in: "))
                postcode = str(input("Enter your Post Code: "))
                telephonenumber = str(input("Enter your Telephone Number: "))
                result = (firstname, lastname, street, town, postcode, telephonenumber)
                ChristmasDatabaseTask.insert_customer(result)
                time.sleep(2)
                customer_process()

        else:
            print("Invalid input, please try again")

menu()


