n=int(input())
li=[]
for i in range(n):
    li.append(int(input()))
n=len(li)
while n>1:
    li.sort()
    smallest=li[0]
    second_smallest=li[1]
    new=(3*smallest+2*second_smallest)%100
    li.remove(smallest)
    li.remove(second_smallest)
    li.append(new)
    n-=1
print(li[0])
