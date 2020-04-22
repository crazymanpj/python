'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''



class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <2:
            return False

        ret = 0
        i = 0
        j = len(height) - 1
        while(i<j):
            area = self.getArea(height, i, j)
            if area > ret:
                ret = area

            if height[i] >= height[j]:
                j = j - 1
            else:
                i = i + 1

        return ret

    def getArea(self, height, i, j):
        index_a = i
        index_b = j
        h = height[index_b] if height[index_a] >= height[index_b] else height[index_a]
        w = index_b - index_a
        return h*w


if __name__ == '__main__':
    s = Solution()
    height=[1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))

'''
[2,3,4,5,18,17,6]
17
'''
