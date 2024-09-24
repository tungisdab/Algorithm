def thn(n,a,b,c):
    if n==1:
        print(a," -> ", c)
        return
    thn(n-1,a,c,b)
    thn(1,a,b,c)
    thn(n-1,b,a,c)
a='A'
b='B'
c='C'
n=int(input())
thn(n,a,b,c)