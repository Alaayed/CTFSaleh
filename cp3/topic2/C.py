MOD = 998244353
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

def possible_permutations(n, fact, invfact):
    # assume stars and bars
    # |*|*|*|*|*
    # stars are n
    # each one must have AT LEAST 1 n
    # one s at the start, it's fixed
    # |* ? * ? *|
    # |* ? * ? * ? *|
    #|* || * || * || * * * * * * *|
    # 1 2 3
    # 4 5 6
    # 2 4 6
    # 1 3 5
    for i in range(1, n+1):
        overcounted_permutations = choose(n-1, i-1, fact, invfact) ** 2
        overcounted_permutations %= MOD
        #
        true_permutations = overcounted_permutations * invfact[]


def solve():
    MAXN = 100
    fact, invfact = build_fact(MAXN, MOD)
    for _ in range(int(input())):
        n,m = map(int, input().split())
        restrictions = [list(map(int(input()))) for _ in range(m)]
        total_permutations = possible_permutations(n, fact, invfact)
        for i in range(1,n+1):

