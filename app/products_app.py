import csv

products = []

products_csv = "/Users/michaelmiles/Desktop/crud-application/data/products.csv"
headers = ["id", "name", "aisle", "department", "price"]
user_input_headers = [header for header in headers if header != "id"]

def get_product_id(product): return int(product["id"])

def auto_incremented_id():
    product_ids = map(get_product_id, products)
    return max(product_ids) + 1

# READ PRODUCTS FROM FILE

with open(products_csv, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for ordered_dict in reader:
        products.append(dict(ordered_dict))

# CRUD OPERATIONS: LIST, SHOW, CREATE, UPDATE, DESTROY

def list_products():
    print("LISTING ALL PRODUCTS")
    for product in products:
        print(" + Product #" + str(product["id"]) + ": " + product["name"])

def show_product():
    product_id = input("WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("READING PRODUCT", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH THAT IDENTIFIER", product)

def create_product():
    print("PLEASE PROVIDE THE PRODUCT'S INFORMATION")
    product = {"id": auto_incremented_id() }
    for header in user_input_headers:
        product[header] = input("The '{0}' is: ".format(header))
    products.append(product)
    print("CREATING PRODUCT", product)

def update_product():
    product_id = input("WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("PLEASE PROVIDE THE PRODUCT'S INFORMATION")
        for header in user_input_headers:
            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
        print("UPDATING PRODUCT", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH THAT IDENTIFIER", product_id)

def destroy_product():
    product_id = input("WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("DESTROYING PRODUCT", product)
        del products[products.index(product)]
    else:
        print("COULDN'T FIND A PRODUCT WITH THAT IDENTIFIER", product_id)

menu = """
-----------------------------------
PRODUCTS APP
-----------------------------------
Welcome to the Products App!
There are {1} products in the database.
    operation | description
    --------- | ------------------
    'List'    | Display a list of product identifiers and names.
    'Show'    | Show information about a product.
    'Create'  | Add a new product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.
Please select an operation: """.format("@mikemiles", len(products))

crud_operation = input(menu)

if crud_operation.title() == "List":
    list_products()
elif crud_operation.title() == "Show":
    show_product()
elif crud_operation.title() == "Create":
    create_product()
elif crud_operation.title() == "Update":
    update_product()
elif crud_operation.title() == "Destroy":
    destroy_product()
else:
    print("THAT IS NOT AN AVAILABLE OPERATION. PLEASE REVIEW THE OPTIONS AND TRY AGAIN.")

# WRITE PRODUCTS TO FILE

with open(products_csv, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()

    for product in products:
        writer.writerow(product)
