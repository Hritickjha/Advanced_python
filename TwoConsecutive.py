def count_consecutive_ones(list):
    count = 0
    total = 0
    for num in list:
        if num == 1:
            count += 1
        if count == 2:
            total += 1
    else:
        count = 0
    return total
elements = input("enter the elements of the list(space-separated):").split()
my_list = [int(elem) for elem in elements]
occurences = count_consecutive_ones(my_list)
print("occurences of two consecutive ones:",occurences)
            
