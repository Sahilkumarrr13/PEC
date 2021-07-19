n=int(input())
i=1
while i<=n:
    for j in range((i-1)*5+1,5*i+1):
        print(j,end=" ")
    i+=1
    print()
    for k in reversed(range((i-1)*5+1,5*i+1)):
        print(k end=" ")
    print()
    i+=1
