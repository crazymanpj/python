#encoding=utf-8
# Date:    2019-12-26
# Author:  pangjian
'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

'''

class Solution:
    def longestCommonPrefix(self, strs):
        pre = ''
        temp = ''
        j = 0
        while(True):
            temp = ''
            for i in range(len(strs)):
                if j > len(strs[i]) - 1:
                    return pre
                # print(strs[i][j])
                if i == 0:
                    temp = strs[i][j]
                elif strs[i][j] != temp:
                    return pre

            pre = pre + temp
            j = j + 1


class Solution_S:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0 or len(strs[0]) == 0:
            return ''
        return self.findindex(strs, 0, len(strs[0]) -1)

    def findindex(self, strs, start, end):
        print(start ,end)
        index = (start + end) // 2
        print(index)
        for i in range(len(strs)):
            if i == 0:
                temp = strs[i][ :index + 1]
            elif index > len(strs[i]) - 1 or strs[i][:index + 1] != temp:
                print('not')
                if start < end:
                    return self.findindex(strs, start, index // 2)
                else:
                    return '' if start == 0 else strs[0][:start]

        print('yes')
        if index + 1 == end:
            return self.findindex(strs, index + 1, end)
        else:
            return strs[0][:start + 1] if start == end else self.findindex(strs, index, end)

if __name__ == '__main__':
    s = Solution_S()
    strs = ["flower","flow","flight"]
    ret = s.longestCommonPrefix(strs)
    print('result')
    print(ret)
