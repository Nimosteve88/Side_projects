import ChristmasDatabaseTask

MENU_PROMPT = """-----Shoppin4Christmas Stock Management System-----
Welcome to Shoppin4Christmas
Please choose one of these options:
1) Add a new Product
2) See all Products
3) Find a Product by Name
4) Delete a Product by Name 
5) Exit

Your Selection: """


def menu():
    connection = ChristmasDatabaseTask.connect()
    ChristmasDatabaseTask.create_product()

    while (user_input := input(MENU_PROMPT)) != "5":
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
        elif user_input == "3":
            name = str(input("Enter the Product Name to find: "))
            products = ChristmasDatabaseTask.select_product(name)

            for product in products:
                print(f"{product[1]}-------({product[2]})-------({product[3]})-------{product[4]}")
        elif user_input == "4":
            name = str(input("Enter the Product Name you want to remove: "))
            ChristmasDatabaseTask.delete_product(name)
        else:
            print("Invalid input, please try again")

menu()