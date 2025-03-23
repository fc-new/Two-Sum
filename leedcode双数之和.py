from typing import List
"""
两种方法来解决两数之和的问题
第一种方法：通过两次循环来遍历整个数组来找出是否两个数之和能达到目标值
第二种方法：引入哈希表，只需要通过一次循环，每次遍历一个数时，将其值作为键，
索引作为值，存入字典，然后判断目标值减去该数的值之后的剩余值是不是在字典里，经过遍历一遍
就能找到有没有
"""

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         num_dict = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_dict:
#                 return [num_dict[complement], i]
#             num_dict[num] = i
#         return []