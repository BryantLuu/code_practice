class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i in range(len(nums)):
            current = nums[i]
            other_half = target - nums[i]
            if other_half in checked:
                return [i, checked[other_half]]
            else:
                checked[current] = i
