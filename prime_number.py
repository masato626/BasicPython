a = int(61)
b=int(10)
if a <= 1:
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
