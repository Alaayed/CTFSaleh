from math import comb
# ?0?
# q_1 = 0,
UPPER_BOUND = 1000000007
def inversions():
    line = input()[::-1]
    zc = 0
    qc = 0
    res= 0
    for c in line:
        if c == '0':
            zc += 1
        elif c == '?':
            res += pascals_triangle(zc,qc) % UPPER_BOUND
            qc += 1
        elif c == '1':
            res += pascals_triangle(zc,qc) % UPPER_BOUND
    return res


def pascals_triangle(zc , qc):
    sum = 0
    for i in range(qc + 1):
        coefficient = i + zc
        invc = coefficient * comb(qc, i)
        sum += invc % UPPER_BOUND
        #print(f'{coefficient} = {invc}')
    return sum

print(inversions())