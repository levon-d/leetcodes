class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float("inf")
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                current = nums[i] + nums[l] + nums[r]

                if abs(target - current) < abs(target - result):
                    result = current

                if current > target:
                    r -= 1
                elif current < target:
                    l += 1
                else:
                    return target

        return result
