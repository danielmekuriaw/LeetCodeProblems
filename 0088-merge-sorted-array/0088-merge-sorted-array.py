class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_n1 = 0;
        index_n2 = 0;

        while (index_n2 < n): # nums2's size doesn't change
            n1 = nums1[index_n1];
            n2 = nums2[index_n2];

            if (index_n1 < m + index_n2):
                if (n1 > n2):
                    nums1.insert(index_n1, n2);
                    nums1.pop(-1);
                    index_n2 += 1;
            else:
                nums1.insert(index_n1, n2);
                nums1.pop(-1);
                index_n2 += 1;
            
            index_n1 += 1
        