#encoding=utf-8
# Date:    2019-10-24
# Author:  pangjian
import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) ==0:
            return self.getmiddlefromarray(nums2)

        if len(nums2) == 0:
            return self.getmiddlefromarray(nums1)

        marray = nums1 + nums2

        marray = sorted(marray)
        return self.getmiddlefromarray(marray)


    def getmiddlefromarray(self, marray):
        if len(marray) % 2 == 0:
            x1 = int(len(marray) / 2 - 1)
            x2 = int(len(marray) / 2)
            print(x1, x2)
            print(marray[x1], marray[x2])
            ret = (float(marray[x1]) + float(marray[x2]))/2
            print(ret)
            return ret

        if len(marray) % 2 == 1:
            return marray[int(len(marray) / 2)]



if __name__ == '__main__':
    s = Solution()
    nums1 =[1,2]
    nums2 =[3,4]
    #print(s.getmiddlefromarray(marray))
    print(s.findMedianSortedArrays(nums1, nums2))
