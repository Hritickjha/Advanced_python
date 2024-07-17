def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
#Taking input from the user
elements = input("Enter the elements of the list(space-separated): ").split
#converting the string list into the integer
my_list = [int(a) for a in elements]
#Taking input from the user to search for the element
target = int(input("Enter the element to search for:"))
index = linear_search(my_list,target)
if index != -1:
    print("element",target,"found at index", index)
else:
    print("element",target,"not found in the list.")
    