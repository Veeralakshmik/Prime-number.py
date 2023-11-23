n=int(input())
c=0
for i in range(1,n):
    for j in range(1,n):
        if(i%j==0):
            c=c+1
if(c==2):
    print(i)

