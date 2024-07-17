import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
P="".join(random.sample(s,passlen))
print(P)