'''create tables'''
import sqlite3

def connect():
    return sqlite3.connect("Shoppin4Christmas.db")

def create_table(db_name, table_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?", (table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("If you are a brand new to this Program then press enter '1' to access the new database or "
                             "enter 2 if you have accessed this Program before  (1/2): ".format(table_name))
            if response == '1':
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing data was kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()


def create_customer():
    db_name = "Shoppin4Christmas.db"
    sql = """create table Customer (
             CustomerID integer,
             FirstName text,
             LastName text,
             Street text,
             Town text,
             PostCode text,
             TelephoneNumber text,
             primary key (CustomerID))"""
    create_table(db_name, "Customer", sql)


def create_product_type():
    db_name = "Shoppin4Christmas.db"
    sql = """create table ProductType (
             ProductTypeID integer,
             Description text,
             primary key (ProductTypeID))"""
    create_table(db_name, "ProductType", sql)


def create_product():
    db_name = "Shoppin4Christmas.db"
    sql = """create table Product (
             ProductID integer,
             Name text,
             Price real,
             Quantity integer,
             ProductTypeID integer,
             primary key (ProductID),
             foreign key (ProductTypeID) references ProductType(ProductTypeID)
             ON UPDATE CASCADE ON DELETE Restrict)"""
    create_table(db_name, "Product", sql)


def create_customer_order():
    db_name = "Shoppin4Christmas.db"
    sql = """create table CustomerOrder (
             CustomerID integer
             Date text,
             Time text,
             ProductName text,
             PriceofProduct real,
             OrderID integer,
             primary key (OrderID),
             foreign key (CustomerID) references Customer(CustomerID)
             ON UPDATE CASCADE ON DELETE Restrict)"""
    create_table(db_name, "CustomerOrder", sql)


def create_order_items():
    db_name = "Shoppin4Christmas.db"
    sql = """create table OrderItem (
             OrderItemID integer,
             OrderID integer,
             ProductID integer,
             primary key (OrderItemID),
             foreign key (OrderID) references CustomerOrder(OrderID)
             ON UPDATE CASCADE ON DELETE Restrict,
             foreign key (ProductID) references Product(ProductID)
             ON UPDATE CASCADE ON DELETE Restrict)"""
    create_table(db_name, "OrderItem", sql)

def query(sql, data):
    with sqlite3.connect("Shoppin4Christmas.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql, data)
        db.commit

def insert_products(records):
    sql = "insert into Product (Name, Price, Quantity, ProductTypeID) values (?,?,?,?)"
    for record in records:
        query(sql, record)

def insert_productTypeID(records):
    sql = "insert into ProductType (Description) values (?)"
    for record in records:
        query(sql, record)



if __name__ == "__main__":
    db_name = "Shoppin4Christmas.db"
    create_customer()
    create_product_type()
    create_product()
    create_customer_order()
    create_order_items()
    product = [('Christmas Food'), ('Christmas Decorations'), ('Christmas Electricals')]
    insert_productTypeID(product)
    products = [('Roast Chicken', 12.0, 24, 1), ('Seafood', 9.0, 20, 1), ('Turkey', 13.00, 24, 1), ('Ham', 6.0, 30, 1),
                ('Salads', 8.0, 20, 1), ('Candles', 15.0, 60, 2), ('Christmas Tree Ornaments', 13.0, 20, 2),
                ('Wreaths', 11.0, 13, 2), ('Ribbons', 6.0, 35, 2), ('Roping', 9.0, 22, 2),('Stream Lights', 20.0, 45, 3),
                ('Stream Lights', 20.00, 45, 3), ('Christmas Tree Lights', 24.00, 40, 3),
                ('LED Fairy String Lights', 25.00, 35, 3), ('Electric Santa Figure', 19.00, 25, 3)]
    insert_products(products)

def insert_data(values):
    with sqlite3.connect("Shoppin4Christmas.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = "insert into 'Product' (Name, Price, Quantity, ProductTypeID) values (?,?,?,?)"
        cursor.execute(sql, values)
        db.commit()

def delete_product(data):
    with sqlite3.connect("Shoppin4Christmas.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = "delete from Product where Name=?"
        cursor.execute(sql,data)
        db.commit()


def select_all_products():
    with sqlite3.connect("Shoppin4Christmas.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product")
        products = cursor.fetchall()
        return products

def select_product(id):
    with sqlite3.connect("Shoppin4Christmas.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product where Name=?",(id,))
        product = cursor.fetchall()
        return product



def customerid(id):
    with sqlite3.connect("Shoppin4Christmas.db") as db:
        cursor = db.cursor()
        cursor.execute("select CustomerID from Customer where LastName=?",(id,))
        product = cursor.fetchone()
        return product

def customer(id):
    with sqlite3.connect("Shoppin4Christmas.db") as db:
        cursor = db.cursor()
        cursor.execute("select LastName from Customer where LastName=?",(id,))
        product = cursor.fetchone()
        return product





def insert_customer(records):
    sql = "insert into Customer (FirstName, LastName, Street, Town, PostCode, TelephoneNumber) values (?,?,?,?,?,?)"
    for record in records:
        query(sql, record)





def autorefill():
    products = [('Roast Chicken', 12.0, 24, 1), ('Seafood', 9.0, 20, 1), ('Turkey', 13.00, 24, 1),
                ('Ham', 6.0, 30, 1),
                ('Salads', 8.0, 20, 1), ('Candles', 15.0, 60, 2), ('Christmas Tree Ornaments', 13.0, 20, 2),
                ('Wreaths', 11.0, 13, 2), ('Ribbons', 6.0, 35, 2), ('Roping', 9.0, 20, 2),
                ('Stream Lights', 20.0, 45, 3),
                ('Stream Lights', 20.00, 45, 3), ('Christmas Tree Lights', 24.00, 40, 3),
                ('LED Fairy String Lights', 25.00, 35, 3), ('Electric Santa Figure', 19.00, 25, 3)]
    insert_products(products)



def insert_customer(values):
    with sqlite3.connect("Shoppin4Christmas.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = "insert into Customer (FirstName, LastName, Street, Town, PostCode, TelephoneNumber) values (?,?,?,?,?,?)"
        cursor.execute(sql, values)
        db.commit()

def insert_orderItem(values):
    with sqlite3.connect("Shoppin4Christmas.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = "insert into OrderItem (OrderID, ProductID) values (?,?)"
        cursor.execute(sql, values)
        db.commit()

def orderHistory(customerID):
    with sqlite3.connect("Shoppin4Christmas.db") as db:
        cursor = db.cursor()
        cursor.execute("select ProductName, PriceofProduct, Date, Time, CustomerID from CustomerOrder where CustomerID=?",(customerID, ))
        products = cursor.fetchall()
        return products


def select_productID(id):
    with sqlite3.connect("Shoppin4Christmas.db") as db:
        cursor = db.cursor()
        cursor.execute("select ProductID from Product where Name=?",(id,))
        product = cursor.fetchone()
        return product

def select_orderID(id):
    with sqlite3.connect("Shoppin4Christmas.db") as db:
        cursor = db.cursor()
        cursor.execute("select OrderID from CustomerOrder where CustomerID=?",(id,))
        product = cursor.fetchone()
        return product