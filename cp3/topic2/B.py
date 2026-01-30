def build_fact(n, mod):
    fact = [1] * (n+1)
    for i in range(1, n+1):
        fact[i] = fact[i-1] * i % mod

    invfact = [0] * (n+1)
    invfact[n] = pow(fact[n], mod - 2, mod)

    for i in range(n-1, -1, -1):
        invfact[i] = invfact[i+1] * (i+1) % mod

    return fact, invfact
def choose (n,k,fact,invfact):
	return fact[n] * invfact[k] * invfact[n-k]


def solve():
    for _ in range(int(input())):
        n,m = map(int, input().split())
        ranges = [list(map(int, input().split())) for i in range(m)]
        unique_values = set()
        # Grab unique possible values for value in a
        for _,_,value in ranges:
            unique_values.add(value)
        print(unique_values)
        # Now, figure out the number of ways that each bit can be set
        # Issue, you CAN figure out the number of subsets where
        # bit i is set,
        # but how do you avoid overcounting?
        # you find it for the first bit,
        # (3,3,3,3,3) ()
        # number of zeros
        # number of odd arranges of 1
        odd_arranges = 1000
        number_zeros = 100
        ans = odd_arranges * 2** number_zeros
        # 0 , 0 , 0 , 0 ,0
        # [0,7,7,0,2]
solve()