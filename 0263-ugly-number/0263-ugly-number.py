class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False;

        if n == 1:
            return True;

        for p in [2, 3, 5]:
            while n % p == 0:
                n = n // p;

        return n == 1;

        

        