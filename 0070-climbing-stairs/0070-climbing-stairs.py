import math

class Solution:
    def climbStairs(self, n: int) -> int:
        num_of_2s = int(n/2);
        num_of_1s = n%2;

        l = num_of_2s + num_of_1s
        count = 0

        while (num_of_2s >= 0):
            count += (math.factorial(l))/(math.factorial(num_of_2s) * math.factorial(num_of_1s))
            num_of_2s -= 1
            num_of_1s += 2
            l = num_of_2s + num_of_1s

        return int(count);