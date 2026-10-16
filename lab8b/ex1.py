# Calculating an extended price for a product (with tax)
product = {
    "name": 'small gumball', 
    "price":'$0.34'
}

tax_rate = 0.045

total = float(product["price"].strip('$')) + float(product["price"].strip('$')) * tax_rate

print(f"A {product['name']} costs {total}")
