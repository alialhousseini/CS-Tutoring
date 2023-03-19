###EX2

def dimension():
    r=int(input("Enter row and column dimensions"))
    return r

def fill_matrices(r):
    X=[]
    Y=[]

    print("Filling 1st matrix X\n")
    for i in range(r):
        temp=int(input(f"Enter the element number {i+1} of X\n"))
        X.append(temp)

    print("Filling 2nd matrix X\n")
    for i in range(r):
        temp=int(input(f"Enter the element number {i+1} of Y\n"))
        Y.append(temp)

    return X,Y

def compute(X,Y):
    inner_product=0
    for i in range(r):
        inner_product = inner_product + X[i]*Y[i]
    return inner_product

def printer(X,Y):
    inner_product = compute(X,Y)
    if inner_product==0:
        print(f"The inner product of X and Y is {inner_product} and they are orthogonal\n")
    else:
        print(f"The inner product of X and Y is {inner_product}\n")


r = dimension()
X,Y = fill_matrices(r)
printer(X,Y)
