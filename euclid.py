 #問3
a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def EachOtherPrime(a,b):
    return gcd(a,b)==1
print("互いに素:",EachOtherPrime(a,b))