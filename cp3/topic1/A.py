from math import gcd
def solve():
    n = int(input())
    nums = list(map(int , input().split()))
    costs = list(map(int, input().split()))
    if gcd(*nums) != 1:
        print(-1)
        return
    zipped = zip(costs, nums)
    zipped = sorted(zipped)
    nums = [num for cost, num in zipped] 
    costs.sort()
    lastPopped = 0
    cpopped = 0
    dontPop = 0
    for _ in range(len(nums)):
        lastPopped = nums.pop(len(nums)-1-dontPop)
        cpopped    = costs.pop(len(costs)-1-dontPop)
        if (gcd(*nums) != 1):
            nums.append(lastPopped)
            costs.append(cpopped)
            dontPop+=1
    print(sum(costs))
solve()