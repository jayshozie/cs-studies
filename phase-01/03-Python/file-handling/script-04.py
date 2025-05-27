# Solution

with open("sample_text.txt", 'r') as input_file, \
     open("filtered_lines.txt", 'w') as output_file:

    for line in input_file:
        tmp = line.lower()
        if "dog" in tmp:
            output_file.write(line)
