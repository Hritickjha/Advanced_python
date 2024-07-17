def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
#clcoding.com
a=60
b=48
print("The gcd of",a,"and",b,"is",gcd(a,b))

