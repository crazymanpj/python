#encoding=utf-8
# Date:    2019-12-25
# Author:  pangjian
'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

输入: "III"       "IV"        "IX"        "LVIII"                     "MCMXCIV"
输出: 3           4           9           58                          1994
示例 2:                                   L = 50, V= 5, III = 3.      M = 1000, CM = 900, XC = 90, IV = 4.
'''
class Solution:
    def romanToInt(self, s):
        num = 0
        speciallist = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        i = 0
        while(i<len(s)):
            print(i)
            if len(s) - i > 1 and (s[i] + s[i+1]) in speciallist:
                num = num + self.getnumber(s[i] + s[i+1])
                i = i + 2
                print('test:' + str(i))
                continue
            else:
                num = num + self.getnumber(s[i])
                i = i + 1
                continue
        if num < 1 or num >3999:
            return 0
        return num

    def getnumber(self, item):
        print(item)
        romelist = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        return romelist[item]

if __name__ == '__main__':
    str_rome = "MCDLXXVI"
    s = Solution()
    print(s.romanToInt(str_rome))
