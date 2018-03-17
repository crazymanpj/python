
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = {}
        for index,item in enumerate(nums):
            hashtable[item] = index

        for index,item in enumerate(nums):
            dif = target - item
            if hashtable.has_key(dif) and hashtable[dif] !=index:
                return [index, hashtable[dif]]


if __name__ =='__main__':
    s = Solution()
    print s.twoSum([3,2,4], 6)
