# Solution

summary = {}

with open("product_sales.csv", 'r') as sales, \
     open("product_summary.txt", 'w') as sales_summary:

    is_header = True
    for line in sales:
        if is_header:
            is_header = False
            continue

        line = line.strip()
        if not line:
            continue

        total_sale = 0.0

        parts = line.split(',')

        product_name = parts[0]
        quantity_sold = int(parts[1])  # Since we know the data is correct
        unit_price = float(parts[2])  # Since we know the data is correct

        total_sale = quantity_sold * unit_price

        """
        Example of summary dict:
        {
            'Laptop': "5,6000.00"
            'Mouse': "10,250.00"
        }
        """

        if product_name not in summary:
            # print(f"DEBUG: 'summary' (dict): {summary}")
            tmp_string = ""
            tmp_string = str(str(quantity_sold) + ',' + str(total_sale))
            summary[product_name] = tmp_string
            # print(f"DEBUG: Product Name Keys: {summary}")
            # print(f"DEBUG: Product Name Value: {summary[product_name]}")

        else:
            tmp_string = ""
            tmp_quantity, tmp_total = summary[product_name].split(',')

            quantity_sold += int(tmp_quantity)
            total_sale += float(tmp_total)

            tmp_string = str(str(quantity_sold) + ',' + str(total_sale))

            summary[product_name] = tmp_string
            # print(f"DEBUG: 'summary' (dict): {summary}")

    sorted_summary = sorted(summary)

    sales_summary.write("Product Sales Summary:\n")
    for product in sorted_summary:
        total_sold, total_revenue = summary[product].split(',')
        sales_summary.write(
            f"{product}: Total Quantity Sold: {total_sold}, "
            f"Total Revenue: ${total_revenue}\n"
        )

"""
Footnote: You could do this task by using tuples for the total_sold and
          total_revenue variables.
          That didn't come to my mind while solving this, thus
          this monstrosity, but it works.
"""
