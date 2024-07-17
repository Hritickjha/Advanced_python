def print_rectangle(rows,cols):
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows -1 or j == 0 or j == cols -1:
               print("*",end="")
            else:
                print("", end="")
            print()
rows = int(input("Enter the number of rows for the rectangle:"))
cols = int(input("Enter the number of columns for the rectanglw:"))
print("Rectangle:")
print_rectangle(rows,cols)

