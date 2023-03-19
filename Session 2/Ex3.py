

def factorial(n):
    num=n
    fact=1
    while num!=0:
        fact*=num
        num-=1
    print(f"The factorial of {n} is {fact}")
n=4
factorial(n)