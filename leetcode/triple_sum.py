#encoding=utf-8
# Date:    2019-01-14
# Author:  pangjian
'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

def twosum(nums, target):
    res = {}
    for i in range(len(nums)):
        res[target - nums[i]] = nums[i]




if __name__ == '__main__':
    print(twosum())
