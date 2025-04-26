from itertools import permutations
from math import factorial

def print_permutations(n):
    nums = list(range(1, n + 1))
    for i, perm in enumerate( permutations(nums)):
        print(f'i: {i+1} , {perm}')
def fact(n):
    res = '[ '
    for i in range(n):
        res += str(factorial(i + 1)) +','
    return res + ' ]'
# Example usage
print_permutations(3)
print(fact(9))
