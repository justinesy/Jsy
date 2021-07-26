products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

get_product("espresso")

def get_property(code, property):
    return products[code][property]

get_property("espresso", "price")

def main():
    totalorder = []
    finaltotal = 0
    aqty = 0
    bqty = 0
    cqty = 0
    dqty = 0
    eqty = 0
    fqty = 0


    while(True):
        order = input("Enter customer's order/s: ")
        if order == "/" :
            break

        else:
            product_code, quantity = order.split(",")

            if product_code == "americano":
                aqty += int(quantity)

            elif product_code == "brewedcoffee":
                bqty += int(quantity)

            elif product_code == "cappuccino":
                cqty += int(quantity)

            elif product_code == "dalgona":
                dqty += int(quantity)

            elif product_code == "espresso":
                eqty += int(quantity)

            elif product_code == "frappuccino":
                fqty += int(quantity)

            finaltotal += get_property(product_code, "price") * int(quantity)

    if aqty != 0:
        totalorder += [("americano", aqty)]

    if bqty != 0:
        totalorder += [("brewedcoffee", bqty)]

    if cqty != 0:
        totalorder += [("cappuccino", cqty)]

    if dqty != 0:
        totalorder += [("dalgona", dqty)]

    if eqty != 0:
        totalorder += [("espresso", eqty)]

    if fqty != 0:
        totalorder += [("frappuccino", fqty)]

    with open("receipt.txt", "w") as f:
        f.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
        ''')

    for items in totalorder:
        code = items[0]
        name = get_property(items[0], "name")
        quantity = items[1]
        total  = get_property(items[0], "price") * quantity

        with open("receipt.txt", "a") as f:
            f.write(f'\n{code}\t\t{name}\t\t{quantity}\t\t\t\t{total}')

    with open("receipt.txt", "a+") as f:
        f.write(f'''
Total:\t\t\t\t\t\t\t\t\t\t{finaltotal}
==
        ''')
        f.seek(0)
        print(f.read())

main()
