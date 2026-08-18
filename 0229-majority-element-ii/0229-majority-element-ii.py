class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        candidate1 = candidate2 = None
        count1 = count2 = 0

        # Find candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Verify candidates
        result = []

        if nums.count(candidate1) > n // 3:
            result.append(candidate1)

        if candidate2 != candidate1 and nums.count(candidate2) > n // 3:
            result.append(candidate2)

        return result