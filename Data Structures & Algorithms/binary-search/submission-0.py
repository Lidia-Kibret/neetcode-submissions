class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = set(nums)
        if target in s:
            return nums.index(target)

        return -1
        
        