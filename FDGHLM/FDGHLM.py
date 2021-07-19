n,k=map(int,input().split())
sn=[];sk=[]
for i in range(1,n+1):
    if n%i==0:
        sn.append(i)
    else:
        pass
for i in range(1,k+1):
    if k%i==0:
        sk.append(i)
    else:
        pass
sn=set(sn);sk=set(sk)
hcf=list(sn.intersection(sk))
HCF=hcf[-1]
LCM=int((n*k)/HCF)
print(HCF,LCM)
