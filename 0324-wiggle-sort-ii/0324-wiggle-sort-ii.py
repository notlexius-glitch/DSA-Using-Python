class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        
        n = len(nums)
        mid = (n - 1) // 2
        right = n - 1
        
        result = [0] * n
        
        for i in range(n):
            if i % 2 == 0:
                result[i] = nums[mid]
                mid -= 1
            else:
                result[i] = nums[right]
                right -= 1
        
        nums[:] = result