# Solution

with open('products.csv', 'r') as products, \
     open('electronics_summary.txt', 'w') as summary:
    total_value = 0
    in_stock_items = []
    for line in products:
        split_line = line.split(',')
        if split_line[0] == "Product Name":
            continue
        # Alternative for skipping the header line
        # is_header = True
        # if is_header:
        #     is_header = False
        #     continue

        in_stock = False

        product_name = split_line[0]
        category = split_line[1]
        price_str = split_line[2]

        try:
            price = float(price_str)
        except ValueError:
            price = 0
            print(f"Warning: Unexpected 'Price' value '{price_str}' "
                  f"for product '{product_name}'. "
                  f"Assuming 0.")

        stock_status_str = split_line[3].strip().lower()
        if stock_status_str == 'true':
            in_stock = True
        elif stock_status_str == 'false':
            in_stock = False
        else:
            in_stock = False
            print(f"Warning: Unexpected 'In Stock' value '{stock_status_str}' "
                  f"for product '{product_name}'. "
                  f"Assuming False.")

        if in_stock and category == "Electronics" and price != 0:
            in_stock_items.append(product_name)
            total_value += price
        elif in_stock and category == "Electronics" and price == 0:
            print(f"Warning: The value of 'Price' of '{product_name}' is '0'.")

    summary.write(f"Total Value of In-Stock Electronics: {total_value:.2f}\n")
    summary.write("In-Stock Electronics Products:\n")
    for item in in_stock_items:
        summary.write(f"{item}\n")
