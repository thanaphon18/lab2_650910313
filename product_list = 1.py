product_list = {}

def add_product(product_list):
    product_name = input("Enter Product Name: ")
    product_quantity = input("Enter Product Quantity: ")
    if product_name in product_list:
        product_list[product_name] += product_quantity
    else:
        product_list[product_name] = product_quantity

def show_product(product_list):
    for key in product_list.keys():
        print(key + " : " + str(product_list[key]))

add_product(product_list)
add_product(product_list)
add_product(product_list)
show_product(product_list)