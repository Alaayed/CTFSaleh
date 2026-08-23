from typing import List
def merge(a, b): return a+b
class NumArray:

    def __init__(self, nums: List[int]):
        t = [0 for _ in range(4*len(nums) + 5)]
        def build(v, l, r):
            if l == r: # is leaf
                t[v] = nums[l]
            else:
                lc, rc = 2*v+1, 2*v+2 # 0 indexed
                mid = (l+r)//2
                build(lc,l , mid)
                build(rc,mid+1 , r)
                t[v] = merge(t[lc] , t[rc])

        build(0, 0, len(nums)-1)
        self.t = t
        self.n = len(nums)

    def update(self, index: int, val: int) -> None:
        t = self.t
        def update(pos, l, r, index, val):
            if l == r == index:
                t[pos] = val
            elif l <= index <= r:
                lc, rc = 2*pos+1, 2*pos+2
                mid = (l+r) // 2
                # Recurse down both
                #print(f'at {pos}, left range is [{l}, {mid}], rc range is [{mid+1}, {r}]... index,val ({index,val})')
                update(lc, l, mid, index, val)
                update(rc, mid+1, r, index, val)
                t[pos] = merge(t[lc], t[rc])

        update(0, 0, self.n-1, index, val)


        

    def sumRange(self, left: int, right: int) -> int:
        t = self.t
        def query(v, l, r, ql, qr):
            if r < ql or qr < l:
                return 0
            elif ql <= l <= r <= qr:
                return t[v]
            else:
                lc,rc = 2*v+1, 2*v+2
                mid = (l+r)//2
                lq = query(lc, l , mid, ql, qr)
                rq = query(rc, mid+1, r, ql, qr)
                return merge(lq, rq)
        return query(0, 0, self.n-1, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# test = NumArray([1,3,5])
# print(test.sumRange(0, 2))
# print(test.t)
# test.update(1,2)
# print(test.t)
# print(test.sumRange(0,2))
