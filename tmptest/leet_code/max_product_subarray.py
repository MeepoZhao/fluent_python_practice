#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/11


# 给定一个数组，找出其中连续子数组最大的乘积
def maxProduct(nums: [int]) -> int:
    res = nums[0]
    maxValue = nums[0]
    minValue = nums[0]
    # 遍历数组，
    for i in range(1, len(nums)):
        maxValueTmp = max(nums[i], maxValue * nums[i], minValue * nums[i])
        minValue = min(nums[i], minValue * nums[i], maxValue * nums[i])
        maxValue = maxValueTmp
        res = max(maxValue, res)
    return res


if __name__ == '__main__':
    # nums = [2, 3, -2, 4]
    nums = [-2, -5, -1]
    print(maxProduct(nums))
