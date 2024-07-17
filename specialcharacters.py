def print_special_pattern_pt2(rows):
    for i in range(1, rows + 1):
        print(" " *(rows -i) + my_input* i)
my_input = input("Enter the special Character:")
num_rows = int(input("Enter the number of rows:"))
print_special_pattern_pt2(num_rows)
