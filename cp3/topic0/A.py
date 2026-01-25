def histogram_solver(b):
    return sum (max(b[i]-b[i-1] , 0) for i in range(1, len(b)))
print(histogram_solver([0,2,3,0,4,3,4,1,3]))
def solve():
    print()
solve()