class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = [];
        k = 0;
        indices = [];

        for i in range(len(nums)):
            n = nums[i];

            if i > 0:
                n1 = nums[i-1];

                if n == n1:
                    indices.append(i);

            if n not in seen :
                k = k + 1;
            
            seen.append(n);

        m = 0;
        for i in indices:
            nums.pop(i-m);
            m = m + 1

        return k;