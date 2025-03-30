def convert(s: str, numRows: int) -> str:
    rows = ['' for _ in range(numRows)]
    cur_row = 0
    down = True;
    for (i, c) in enumerate(s):
        #print(f"rows: {rows}")
        rows[cur_row] += c
        #print(f"row {cur_row}: {rows[cur_row]}")
        if down:
            cur_row += 1
            if cur_row == numRows:
                down = False
                cur_row = max(numRows - 2, 0)
        else:
            cur_row -= 1
            if cur_row < 0:
                down = True
                cur_row = min(numRows - 1, 1)
    return ''.join(rows)
tests = input()
for _ in range(int(tests)):
    s , n = input().split()
    res = convert(s, int(n))

    print(res)

