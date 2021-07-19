n,k=map(int,input().split())
if n%2==0:
    if k%2==0:
        for i in range(n+1,k,2):
            print(i,end=" ")
    else:
        for i in range(n+1,k+1,2):
            print(i,end=" ")
else:
    if k%2==0:
        for i in range(n,k,2):
            print(i,end=" ")
    else:
        for i in range(n,k+1,2):
            print(i,end=" ")
