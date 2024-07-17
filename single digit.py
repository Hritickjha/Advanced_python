def get_single_digit(number):
    if len(number) == 1 and number.isdigit():
        return True
    else:
        return False
while True:
    input_number = input("enter a number:")
    if get_single_digit(input_number):
        print("valid single digit")
        break
    else:
        print("Not a valid single digit.Try again.")
print("single digit you enter is :", input_number)
