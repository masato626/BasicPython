a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
if a<b:
    x=b
    y=a
else:
    x=a
    y=b

while b!=0:
    q=a//b
    r=a%b
    a=b
    b=r

print(a)