def dict_shopping(ls):
    price = 0
    qtt = 0
    for i in ls:
        if "price" in i and "quantity" in i and \
                i["price"] >= 0.01 and i["quantity"] >= 1:
            price += i.get("price")*i.get("quantity")
            qtt += i.get("quantity")
        else:
            return ('Invalid JSON', 0)
    return ('${}'.format(round(price, 2)), qtt)
