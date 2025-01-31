class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x;

        left = 1;
        right = x;

        while left <= right:
            mid = (left + right) // 2
            mid_2 = mid * mid;

            if mid_2 == x:
                return mid;
            elif mid_2 < x:
                left = mid + 1
            elif mid_2 > x:
                right = mid - 1

        return right;
