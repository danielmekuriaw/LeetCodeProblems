class Solution:
    def romanToInt(self, s: str) -> int:
        RomToInt = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000};
        result = 0;
        prev = [];

        for c in s:
            if (len(prev) != 0):
                if c == 'V' and prev[-1] == 'I':
                    result -= RomToInt[prev[-1]];
                    result += 4;
                elif c == 'X' and prev[-1] == 'I':
                    result -= RomToInt[prev[-1]];
                    result += 9;
                elif c == 'L' and prev[-1] == 'X':
                    result -= RomToInt[prev[-1]];
                    result += 40;
                elif c == 'C' and prev[-1] == 'X':
                    result -= RomToInt[prev[-1]];
                    result += 90;
                elif c == 'D' and prev[-1] == 'C':
                    result -= RomToInt[prev[-1]];
                    result += 400;
                elif c == 'M' and prev[-1] == 'C':
                    result -= RomToInt[prev[-1]];
                    result += 900;
                else:
                    result += RomToInt[c];
            else:
                result += RomToInt[c];
            
            prev.append(c);

        return result;