class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums);
        m = int(l/2);

        if nums[m] == target:
            return m;

        elif l == 1:
            if target > nums[0]:
                return 1;
            else:
                return 0;

        elif nums[m] < target:
            return m + self.searchInsert(nums[m:], target);
            
        else:
            return self.searchInsert(nums[:m], target);