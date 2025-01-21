class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_val = 0;
        a_exp = 0;
        for i in range(len(a)-1, -1, -1):
            a_val = a_val + (int(a[i]) * (2 ** a_exp))
            a_exp += 1
        
        b_val = 0;
        b_exp = 0;
        for i in range(len(b)-1, -1, -1):
            b_val = b_val + (int(b[i]) * (2 ** b_exp))
            b_exp += 1

        result = str(bin(a_val + b_val)[2:]);
        return result;