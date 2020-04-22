#encoding=utf-8
# Date:    2019-10-30
# Author:  pangjian
'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。---重点

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # print('-'*20)
        # print('s: ' +s)
        # print('p: ' +p)
        # print('-'*20)
        if p == '':
            return s == '' and p == ''

        if s == '':
            if len(p) >=2:
                firstmatch = p[0] == '' or (p[1] == '*' and p[0] == '.')
            else:
                # firstmatch = p[0] == ''
                # if not firstmatch
                # print('test1')
                # print(p[0] == '')
                return p[0] == ''
        else:
            firstmatch = p[0] in [s[0], '.'] 

        # print(firstmatch)
        if p[1:] !='' and p[1] == '*':
            # print(s, p[2:])
            # print(s[1:], p[0:])
            # print('-'*20)
            con = firstmatch and len(s) > 0
            return self.isMatch(s[0:], p[2:]) or (con and self.isMatch(s[1:], p[0:]))
        else:
            # print('normal')
            return firstmatch and self.isMatch(s[1:], p[1:])


str = 'aaaaaaaaaaaaab'
p = "a*a*a*a*a*a*a*a*a*a*c"
s = Solution()
print(s.isMatch(str, p))
