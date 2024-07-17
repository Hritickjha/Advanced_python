def print_letter_F(rows):
    for row in range(rows):
        for col in range(rows):
            if col == 0 or (row == 0 or row == rows //2):
                print("*", end="")
            else:
                print("",end="")
            print()
rows = int(input("Enter the number of rows for the letter F:"))
print_letter_F(rows)
