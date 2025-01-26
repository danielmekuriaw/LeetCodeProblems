class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n == 0):
            return False;
        elif (n == 1):
            return True;
        else:
            if (n % 4 == 0):
                return self.isPowerOfFour(int(n/4));
            else:
                return False;