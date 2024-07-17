def non_zero(matrix):
    max_count = 0
    max_row = None
    for row in matrix:
        count = sum(1 for elem in row if elem != 0)
        if count > max_count:
            max_count = count
            max_row = row
        return max_row
rows = int(input("Enter the number of rows in the matrix:"))
cols = int(input("Enter the number of columns in the matrix:"))
matrix =[]
print("\n")
print("Enter matrix elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i},{j}):"))
        row.append(element)
        matrix.append(row)
print("Matrix :")
for row in matrix:
    print(row)
result = non_zero(matrix)
print("Row with the most non-zero elements is :", result)
