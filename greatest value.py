def find_greatest(list):
    if not list:
        return None
    greatest = list[0]
    for num in list:
        if num>greatest:
            greatest = num
    return greatest
elements = input("enter the elements of the list(space-separated):").split()
my_list = [int(elem)for elem in elements]
result = find_greatest(my_list)
print(my_list,sep=",")
print("The greatest element in the list is:",result)
