a=float(input("a の値を入力: "))
def prime(a):
    if a <= 1:
        print("素数でない")
    elif a!=int:
        print("素数でない")
    else:
        is_prime = True
        for i in range(2, a):
            if a % i == 0:
                is_prime = False
                break
        if is_prime:
            print("素数")
        else:
            print("素数でない")
prime(a)