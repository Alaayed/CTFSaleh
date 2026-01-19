def twoPointer(nums,k):
    L = 0
    smallestRange = 10 ** 6
    curSum = 0
    lookups = dict()
    for i in range(len(nums)):
        lookups[nums[i]] = lookups.get(nums[i], 0) + 1

        curSum += nums[i] if lookups[nums[i]] == 1 else 0
        while(curSum >= k):
            # Record Range
            smallestRange = min(smallestRange, i-L + 1)
            # Update lookups
            lookups[nums[L]] -= 1
            curSum -= nums[L] if lookups[nums[L]] == 0 else 0
            L +=1 
    return smallestRange if smallestRange != 10 ** 6 else -1

l = [[2,2,3,1],
4,
[3,2,3,4],
5,
[5,5,4],
5,]
for i in range(0 , len(l), 2):
    n,k = l[i], l[i+1]
    print(n,k)
    print(twoPointer(n, k))
