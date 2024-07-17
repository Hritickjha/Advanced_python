#get vowels in python
def get_vowels(String):
    return[each for each in String if each in "aeiou"]
word = input("enter a word to check vowels:")
get_vowels(word)
#capitalizing firstLetter
def capitalize(string):
    return string.title()
word = input("Enter a word to captalize: ")
capitalize(word)
#print string N Times
n = int(input("Enter no times to print :"))
string=input("Enter a word :")
print(string*n)
