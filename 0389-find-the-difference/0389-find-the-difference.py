class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t;

        diff = "";

        s_dict = {};
        t_dict = {};

        for c in s:
            if c in s_dict:
                s_dict[c] += 1;
            else:
                s_dict[c] = 1;

        for c in t:
            if c in t_dict:
                t_dict[c] += 1;
            else:
                t_dict[c] = 1;

        for t_key in t_dict:
            if t_key in s_dict:
                if t_dict[t_key] != s_dict[t_key]:
                    diff = t_key;
            else:
                diff = t_key;


        return diff;
        
