# Solution

# This solution is basically error handling fetish.

import sys

valid_records_count = 0
total_revenue = 0.0
processed_sales_records = []

try:
    with (open('sales_data.csv', 'r') as data, \
          open('sales_summary.txt', 'w') as summary):

        is_header = True

        for line in data:
            line = line.strip()
            print(f"DEBUG: Processing line: '{line}'")

            if not line:  # Skip empty lines
                print("DEBUG: Skipping empty line.")
                continue

            if is_header:  # Skip header row
                is_header = False
                continue

            parts = line.split(',')

            if len(parts) != 4:  # Validate number of fields
                print(f"Warning: Skipped malformed line "
                f"(unexpected number of fields): '{line}'")
                continue

            region_raw = parts[0].strip()
            product_raw = parts[1].strip()
            units_sold_str = parts[2].strip()
            revenue_str = parts[3].strip()

            units_sold = 0
            revenue = 0.0

            try:  # Convert data types and handle conversion errors
                units_sold = int(units_sold_str)
                revenue = float(revenue_str)
            except ValueError:
                print(f"Warning: Skipping line with non-numeric data: '{line}'")
                continue

            valid_records_count += 1
            total_revenue += revenue

            processed_sales_records.append({
                'region': region_raw,
                'product': product_raw,
                'units_sold': units_sold,
                'revenue': revenue
            })

        summary.write(f"Total Valid Records: {valid_records_count}\n")
        summary.write(f"Total Revenue: ${total_revenue:.2f}\n")
        summary.write("Processed Sales Records:\n")

        for record in processed_sales_records:
            summary.write(
                f"{record['region']} - {record['product']}: "
                f"{record['units_sold']} units, Revenue: ${record['revenue']:.2f}\n"
            )



except FileNotFoundError:  # Handling FileNotFoundError error
    print("Warning: sales_data.csv not found. Aborting.")
    sys.exit(404)
except Exception as e:  # Handling any other error
    print(f"Warning: An unexpected error occurred while processing the file: {e}")
    sys.exit(101)

print("\nProcessing complete. Check 'sales_summary.txt' for the report.")
