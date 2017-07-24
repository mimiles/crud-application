import csv

products = []

csv_file_path = "/Users/michaelmiles/Desktop/crud-application/data/products.csv"

# READ PRODUCTS CSV

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

menu = """
    Hi.

    Welcome to the products app.

    There are {0} products.

    Available operations: 'List', 'Show', 'Create', 'Update', 'Destroy'

    Please choose an operation:

""".format(len(products))

chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

def list_products():
    print("LISTING PRODUCTS")
    #IMPLEMENT THE LIST OPERATION


def show_product():
    print("SHOWING A PRODUCT")
    #IMPLEMENT THE SHOW OPERATION
    #show_product = [product for product in products if product["id"] == product_id]
    #return show_product[0]

def create_product():
    print("CREATING A PRODUCT")
    product_name = input("name is:")
    product_aisle = input("aisle is:")
    product_department = input("department is:")
    product_price = input("price is:")
    new_product = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    print("NEW PRODUCT IS", new_product)
    products.append(new_product)
    #IMPLEMENT THE CREATE OPERATION

def update_product():
    print("UPDATING A PRODUCT")
    #IMPLEMENT THE UPDATE OPERATION AS FINAL STEP IN CHECKPOINT III

def destroy_product():
    print("DESTROYING A PRODUCT")
    #IMPLEMENT THE DESTROY OPERATION

if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")


# OVERWRITING INVENTORY CSV FILE

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)

#IMPLEMENT SHOW OPERATION

show_product = [product for product in products if product["id"] == product_id]
    return matching_products[0]
