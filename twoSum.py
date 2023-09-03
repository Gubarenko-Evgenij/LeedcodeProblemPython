# условие задачи https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        """twoSum возвращает два числа, сумма которых равна target

        :nums: массив целых чисел
        :target: целое число
        :return: возвращает список - индексы двух чисел
        """
        for i in range(len(nums)-1):
            temp = target-nums[i]
            if nums[i+1:].count(temp):
                return [i,nums.index(temp,i+1)]
        return [0,0]
