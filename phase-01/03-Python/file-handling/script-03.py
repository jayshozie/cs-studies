# Solution

with open("sample_text.txt", 'r') as input_file, \
     open("processed_output.txt", 'w') as output_file:

    for line in input_file:
        processed_line = line.upper()

        processed_line = "PROCESSED: " + processed_line

        output_file.write(processed_line)

with open("processed_output.txt", 'r') as output_file:
    print("\n---- Content of processed_output.txt ---\n")
    print(output_file.read())
    print("-" * 40)
