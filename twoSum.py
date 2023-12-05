# условие задачи https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        """twoSum возвращает два числа, сумма которых равна target

        :nums: массив целых чисел
        :target: целое число
        :return: возвращает список - индексы двух чисел
        """
        if type(nums) is not list:
            raise ValueError("Первый параметр должен быть списком")
        if type(target) != int or all(type(item) is not int for item in nums) or target < 0 or all(
                item < 0 for item in nums):
            raise ValueError("Тип параметров должен быть int неотрицательным")
        try:
            for i in range(len(nums) - 1):
                temp = target - nums[i]
                if nums[i + 1:].count(temp):
                    return [i, nums.index(temp, i + 1)]
            return [0, 0]
        except():
            raise ValueError("Что-то пошло не так")
