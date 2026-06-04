class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m=set(nums)
        if len(m)<len(nums):    
            return True
        else:
            return False

        