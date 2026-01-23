n = int(input())
res = [0 for _ in range(n)]
for j in range(1,n+1):
    for i in range(n):
        res [(i - (j-1)) % n] +=1
print(res)