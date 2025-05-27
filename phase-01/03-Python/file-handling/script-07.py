# Solution

with open('products.csv', 'r') as products, \
     open('category_counts.txt', 'w') as output:

    categories = {}
    is_header = True
    for line in products:
        if is_header:
            is_header = False
            continue

        line = line.strip()
        if not line:
            continue

        parts = line.rsplit(',', 3)

        product_name_raw = parts[0]
        category_raw = parts[1]
        price_str_raw = parts[2]
        stock_status_str_raw = parts[3]

        product_name = product_name_raw.strip('"')
        category = category_raw.strip()
        price_str = price_str_raw.strip()
        stock_status_str = stock_status_str_raw.strip()

        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

    output.write("Product Category Counts:\n")
    for category_name, count in categories.items():
        output.write(f"{category_name}: {count}\n")
