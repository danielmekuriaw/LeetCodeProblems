class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n == 0):
            return False;
        elif (n == 1):
            return True;
        else:
            if (n % 2 == 0):
                return self.isPowerOfTwo(int(n/2));
            else:
                return False;