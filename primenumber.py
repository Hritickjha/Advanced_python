def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
#clcoding.com
num = 7
if is_prime(num):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
    
