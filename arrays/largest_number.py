class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        if len(nums) == 1:
            return str(nums[0])

        nums = [str(num) for num in nums]
        nums.sort()
        final = [nums[0]]
        for i in range(1, len(nums)):
            if (nums[i] + final[0]) > (final[0] + nums[i]):
                final = [nums[i]] + final
            else:
                correct_index = 0
                while correct_index < len(final) and (nums[i] + final[correct_index]) < (final[correct_index] + nums[i]):
                    correct_index += 1
                final = final[:correct_index] + [nums[i]] + final[correct_index:]

        return final[0][0] if final[0][0] == "0" else "".join(final)
