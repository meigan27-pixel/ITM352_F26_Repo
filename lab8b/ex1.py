# Calculating an extended price for a product (with tax)
product = {
    "name": 'small gumball', 
    "price":'$0.34'
}

tax_rate = 0.045
#price was considered a string, so need to remove '$' and convert to float
total = float(product["price"].strip('$')) + float(product["price"].strip('$')) * tax_rate
#needed to change how to get product name to print the right name
print(f"A {product['name']} costs {total}")
