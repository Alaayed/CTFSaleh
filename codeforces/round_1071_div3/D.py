
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        for i in range(n):
            arr.append((1<<(n-i))-1)
        for i in range(2, 1 << n):
            # checks if i == 2**?-1
            if not (i.bit_count() == i.bit_length()) and (i % 2 == 1):
                arr.append(i)
        arr.append(0)
        for i in range(1, 1 << n):
            if not  (i.bit_count() == i.bit_length()) and not(i % 2 == 1):
                arr.append(i)

        print(' '.join(list(map(str, arr))))
solve()