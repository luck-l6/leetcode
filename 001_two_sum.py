"""
第1题：两数之和
https://leetcode.com/problems/two-sum/

给定一个数组和一个目标值，找出两个数相加等于目标值，返回它们的下标。

示例：
输入: nums = [2, 7, 11, 15], target = 9
输出: [0, 1]
解释: nums[0] + nums[1] = 2 + 7 = 9

解题思路：
1. 暴力法：两个 for 循环，遍历所有两数组合
   时间复杂度 O(n²)，空间复杂度 O(1)
2. 哈希表法：边遍历边记录见过的数，查找 target - num 是否在哈希表中
   时间复杂度 O(n)，空间复杂度 O(n)
"""


# 方法1：暴力法
def two_sum_brute(nums, target):
    """
    遍历所有可能的两数组合，找到和等于目标值的两个数
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# 方法2：哈希表法（推荐）
def two_sum(nums, target):
    """
    用字典记录见过的数，边遍历边查找
    时间复杂度 O(n)，空间复杂度 O(n)
    """
    seen = {}  # 哈希表：数值 -> 下标

    for i, num in enumerate(nums):
        need = target - num  # 需要找的另一个数
        if need in seen:     # 之前见过吗？
            return [seen[need], i]
        seen[num] = i        # 没见过，记录下来


# 测试
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # 输出: [0, 1]
