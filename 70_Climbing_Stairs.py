class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        s1, s2 = 1, 2
        for _ in range(n - 2):
            s1, s2 = s2, s1+ s2
        return s2

"""
Way(n) = Way(n-1) + Way(n-2)
Way(n-1) = Way(n-2) + Way(n-3)
.
.
.
Way(3) = Way(2) + Way(1)
"""
# 上面假定到 n - 2 階的算法，因為 n - 2 階後到n階走法固定 （只能走 1, 1 or 2)
# 下面比較直觀

class Solution2:
    def climbStairs(self, n: int) -> int:
        prev, curr = 0, 1
        for _ in range(n):
            prev, curr = curr, prev + curr
        return curr
