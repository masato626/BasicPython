a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

while b!=0:
    q=a//b
    r=a%b
    a=b
    b=r

print(a)