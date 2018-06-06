import csv
import os

def menu(username="@shanyue", products_count=20):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
    Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu

def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []
    #TODO: open the file and populate the products list with product dictionaries
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
            products.append(row)

    return products

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #TODO: open the file and write a list of dictionaries. each dict should represent a product.
    print("Writing to", filepath)
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader() 
        for p in products:
            writer.writerow({"id": p["id"], "name": p["name"], "aisle": p["aisle"], "department": p["department"], "price": p["price"]})
       

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)
    print("Reset has been completed.")
    quit()


def run():
    # First, read products from file...
    products = read_products_from_file()

    # Then, prompt the user to select an operation...
    print(menu(username="@shan")) #TODO instead of printing, capture user input

    print("Please select an operation")
    operation = input()

    # Then, handle selected operation: "List", "Show", "Create", "Update", "Destroy" or "Reset"...
    #TODO: handle selected operation
    if operation == "Show":
        print("---------------")
        print("SHOWING A PRODUCT")
        print("---------------")
        product_id = input("what is the product id")
        print(product_id)
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        if not matching_products:
            print("Product Not Found")
        else:
            matching_product = matching_products[0]
            print(matching_product["name"], matching_product["aisle"], matching_product["department"], matching_product["price"])

    

    elif operation == "Create":
        print("---------------")
        print("CREATING A PRODUCT")
        print("---------------")
        new_id = int(products[-1]["id"]) + 1
        new_name = input("please input the product name ")
        new_aisle = input("please input the product aisle ")
        new_dept = input("please input the product department ")
        new_price = input("please input the product price ")

        new_product = {
            "id": new_id,
            "name": new_name,
            "aisle": new_aisle,
            "department": new_dept,
            "price": new_price
        } 
        products.append(new_product)
        print("CREATING A NEW PRODUCT", new_product)



    elif operation == "Update": 
        product_id = input ("what's the product id?")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        if not matching_products:
            print("Product Not Found")
        else:
            matching_product = matching_products[0]
            matching_product["name"] = input("please input the new product name ")
            matching_product["aisle"] = input("please input the new aisle name ")
            matching_product["department"] = input("please input the new department name ")
            matching_product["price"] = input("please input the new price ")
            print("YOU'VE UPDATED THE PRODUCT")


    elif operation == "List": 
        print("---------------")
        print("LISTING 20 PRODUCTS")
        print("---------------")
        for items in products:
            print(items["id"], items["name"])

    elif operation == "Reset":
        reset_products_file()


    elif operation == "Destroy": 
        product_id = input ("what's the product id?")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        if not matching_products:
            print("Product Not Found")
        else:
            matching_product = matching_products[0]
            products.pop(products.index(matching_product))
            print(matching_product["name"], matching_product["aisle"], matching_product["department"], matching_product["price"])
            print("YOU'VE DESTROYED THE PRODUCT")

    
    
    else:
        print("SORRY, WE DON'T RECOGNIZE THE INPUT")
    
  


    # Finally, save products to file so they persist after script is done...
    write_products_to_file(products=products)

# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()
