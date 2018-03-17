# encoding=utf-8
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
#数组长度一致吗

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = []
        incount = 0
        l1_temp = l1.next
        l2_temp = l2.next
        val, incount = self.getnewnumber(self.getlistnotevalue(l1), self.getlistnotevalue(l2), 0)
        l_new = ListNode(val)
        l_new_temp = l_new

        while(l1_temp != None or l2_temp != None or incount !=0):
            if(l1_temp == None and l2_temp == None):
                val,incount = incount,0
            else:
                val, incount = self.getnewnumber(self.getlistnotevalue(l1_temp), self.getlistnotevalue(l2_temp), incount)

            while(l_new_temp.next != None):
                l_new_temp = l_new_temp.next
            l_new_temp.next = ListNode(val)
            if(l1_temp != None):
                l1_temp = l1_temp.next
            if(l2_temp != None):
                l2_temp = l2_temp.next

        ret.append(l_new.val)
        listnodetemp = l_new.next
        while(listnodetemp != None):
            ret.append(listnodetemp.val)
            listnodetemp = listnodetemp.next
        return ret

    def getnewnumber(self, val1, val2, incount):
        val = val1 + val2 + incount
        if(val >= 10):
            incount = 1
            val = val - 10
        else:
            incount = 0

        return val, incount

    def getlistnotevalue(self, ln):
        if ln == None:
            return 0
        else:
            return ln.val

if __name__ == '__main__':
    s = Solution()
    temp = s
    print id(s)
    print id(temp)

    l1 = ListNode(1)
    l1.next = ListNode(8)

    l2 = ListNode(0)

    ret = s.addTwoNumbers(l1, l2)
    print ret
