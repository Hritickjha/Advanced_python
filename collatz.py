def collatz(n):
    inc = 1
    c = []
    c.append(n)
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = (3*n)+1 
            c.append(n)
        return c
j = int(input("Enter the digit:"))
print(collatz(j))
 