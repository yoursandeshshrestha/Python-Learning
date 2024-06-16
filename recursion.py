def check(n):
    if(n==0):
        return
    print(n)
    check(n-1)

check(5)