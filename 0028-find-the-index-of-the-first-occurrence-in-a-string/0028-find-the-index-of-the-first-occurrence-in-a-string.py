class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh = len(haystack);
        ln = len(needle);
        h = 0;

        if ln > lh:
            return -1;

        while h < lh:
            n = 0;
            initial = h;
            flag = True;

            while n < ln and h < lh:
                print("n: ", n, needle[n]);
                print("h: ", h, haystack[h]);

                if haystack[h] != needle[n]:
                    flag = False;
                    h = initial;
                    break;

                h += 1;
                n += 1;
            
            if flag:
                if (haystack[initial : initial + ln] == needle):
                    return initial;
                else:
                    return -1;

            h += 1;

        return -1;

