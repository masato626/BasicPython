 #問3
a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))
def gcd(a,b):
    while b!=0:
        q=a//b
        r=a%b
        a=b
        b=r
    return a
gcd(a,b)
#問４
def EachOtherPrime(a,b):
    if gcd(a,b)==1:
        print("互いに素")
    else:
        print("互いに素でない")
EachOtherPrime(a,b)