class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            ret = ret + nums[i]

        return ret


if __name__ == "__main__":
    s = Solution()
    print s.arrayPairSum([2,4,6,7,8,9,5,13])
