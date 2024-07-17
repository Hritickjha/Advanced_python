def create_matrix(rows,columns):
    matrix = []
    num = 1
    for a in range(rows):
        row = []
        for a in range(columns):
            row.append(num)
            num += 1 + a
            matrix.append(row)
        return matrix
rows = int(input("Enter the number of rows:"))
columns = int(input("enter the number of columns: "))
matrix = create_matrix(rows,columns)
for ro in matrix:
    print(ro)
    