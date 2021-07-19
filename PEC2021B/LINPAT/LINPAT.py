n=int(input())
pat1=10
pat2=2
for i in range(n):
    if i%2==0:
        print(pat1,end=" ")
        pat1+=10
    else:
        print(pat2,end=" ")
        pat2+=2
