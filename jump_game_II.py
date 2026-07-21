class Solution(object):
    def jump(self, nums):
        jumps = 0
        current_end = 0
        max_farthest = 0

        for i in range(len(nums) - 1):
            max_farthest = max(max_farthest, i + nums[i])
            if (i == current_end):
                jumps += 1
                current_end = max_farthest

        return jumps

nums = [2,3,1,1,4]
sol = Solution()
print(sol.jump(nums))