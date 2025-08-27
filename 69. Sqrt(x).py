class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x // 2

        if x == 1:
            return 1
        elif x == 0:
            return 0

        while left <= right:
            mid = (right + left) // 2
            sqrt = mid * mid

            if sqrt == x:
                return mid
            elif sqrt < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
