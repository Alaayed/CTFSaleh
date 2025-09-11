from math import comb
# ?0?
# q_1 = 0,
UPPER_BOUND = 1000000007
def inversions():
    line = input()
    for i in range(1 , len(line)+1):
        for j in range(i+1 , len(line)+1):
            if line[-i] == '1' and line[-j] == '0':

print(inversions())