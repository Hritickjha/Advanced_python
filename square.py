# using a for loop
numbers = [1,2,3,4,5]
squared_number = []
for num in numbers:
    squared_number.append(num ** 2)
print(squared_number)
# using a list comprehension
numbers = [1,2,3,4,5]
squared_number=[num ** 2 for num in numbers]
print(squared_number)
#using the map() function with lambda
numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
#using the map() function with a decimal function
numbers = [1,2,3,4,5]
def square(x):
    return x**2
squared_numbers = list(map(square,numbers))
print(squared_number)
# using a generator expression
numbers = [1,2,3,4,5]
squared_number = (num **2 for num in numbers)
squared_number = list(squared_number)
print(squared_number)
# using a list compreshension with zip()
numbers =(1,2,3,4,5)
squared_number = [num ** 2 for num in numbers]
print(squared_number)
#using  a loop with enumeration
numbers = [1,2,3,4,5]
square_numbers = []
for i, num in enumerate(numbers):
    square_numbers.append(numbers[i]**2)
print(squared_numbers)
    