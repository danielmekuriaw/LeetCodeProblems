class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indices = []
        n = 0;

        for i in range(len(nums)):
            if nums[i] == val:
                indices.append(i);
            else:
                n = n+1;

        k = 0;
        for i in range(len(indices)):
            if i == 0:
                nums.pop(indices[i]);
            else:
                nums.pop(indices[i] - k)
            k = k+1
        
        return n;