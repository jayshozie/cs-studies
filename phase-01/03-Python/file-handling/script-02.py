# Part A
with open("sample_text.txt", 'r') as sample:
    # First Memory-Inefficient Way:
    all_lines = sample.readlines()  # Store all lines in a list in memory
    print(all_lines[2])  # Print 3rd line

    # Second Memory-Efficient Way:
with open("sample_text.txt", 'r') as sample:
    first_line = sample.readline()
    second_line = sample.readline()
    third_line = sample.readline()
    print(third_line)
    # Not sure about this solution.

# ------------------------------------------

# Part B
with open("sample_text.txt", 'r') as sample:
    # First Memory-Inefficient Way:
    all_lines = sample.readlines()
    print(len(all_lines))

    # Second Memory-Efficient Way:
with open("sample_text.txt", 'r') as sample:
    total_line_num = 0
    for line in sample:
        total_line_num += 1
    print(total_line_num)
    # Not sure about this solution.
