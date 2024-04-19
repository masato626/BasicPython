import math 


def f(x):
    return math.sin(x)
def g(x):
    return 4/(1+x**2)
def h(x):
    return math.pi**(0.5)*math.exp(-x**2)
def tra(a,b,N,f):
    h=(b-a)/N
    s=0
    for k in range(1,N+1):
        s+=h/2*(f(a+(k-1)*h)+f(a+k*h))

    return s
result1=tra(0,math.pi/2,50,f)
result2=tra(0,1,100,g)
result3=tra(-100,100,1000,h)

print("(1)",result1)
print("(2)",result2)
print("(3)",result3)
=======
# --example--
# print(sin(0))
# >>> 0
# -----------
a=0
b=math.pi/2
N=100
h=(b-a)/N
s=0
for k in range(1,N+1):
    s+=h/2*(sin(a+(k-1)*h)+sin(a+k*h))

