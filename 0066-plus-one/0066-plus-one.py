class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0;
        exp = 0;

        for i in range(len(digits)-1, -1, -1):
            result = result + (digits[i] * (10 ** exp));
            exp = exp + 1;

        val = result + 1;
        val_str = str(val);
        arr = []

        for c in val_str:
            arr.append(int(c));

        return arr;