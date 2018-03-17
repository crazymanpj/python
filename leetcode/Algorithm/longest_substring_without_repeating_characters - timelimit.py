# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
            
        for i in range(len(s), 0, -1):
            for j in range(0, len(s)-i+1 ):
                if self.ishasamestr(s[j : j + i]) == False:
                    return len(s[j : j + i])


    def ishasamestr(self,s):
        newstr = set()
        for i in s:
            newstr.add(i)

        if len(s) == len(newstr):
            return False
        else:
            return True

s = Solution()
print s.lengthOfLongestSubstring("")
# print s.ishasamestr('pwwkew')
