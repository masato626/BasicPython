a=float(input("a の値を入力: "))
def prime(a):
    if a <= 1:
        return False
    if int(a)!=a:
        return False
    for i in range(2, int(a)):
        if a % i == 0:
            return False
    return True
print("素数",prime(a))
            
        
        