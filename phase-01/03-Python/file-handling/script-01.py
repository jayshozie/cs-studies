with open("test_file.txt", "r") as test_file:
    print("--- Entire file content as a single string ---")
    all_content = test_file.read()
    print(all_content)
    print("-" * 40)

with open("test_file.txt", "r") as test_file:
    print("--- Content read line by line ---")
    all_lines = test_file.readlines()
    print(str(all_lines))
    single_line = []
    for line in all_lines:  # This is not a good way to read big files.
        # Because it loads the entire file to the memory.
        print(line.strip())
        single_line.append(line.strip())
    print(str(single_line))
    print("-" * 40)

with open("test_file.txt", "r") as test_file:
    # This is the memory-efficient way of reading the entire file line by line.
    print("--- Content read line by line ---")
    for line in test_file:
        print(line.strip())
    print("-" * 40)
"""
with open("output.txt", "w") as output:
    # Write mode wipes the entire file to zero bytes before writing.
    output.write("Hello, Python file handling!")

with open("output.txt", "a") as output:
    # Append mode writes to the end of the file.
    output.write("\nThis is appended content.")
"""
