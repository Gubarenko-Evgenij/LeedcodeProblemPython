from unittest import TestCase, main
import twoSum
class Test_twoSum(TestCase):
    def test_positive_4(self):
        """Позитивный на 4 параметра"""
        self.assertEqual(twoSum.Solution().twoSum([2, 7, 11, 15], 9),[0,1])
    def test_positive_3(self):
        """Позитивный на 3 параметра"""
        self.assertEqual(twoSum.Solution().twoSum([3,2,4], 6),[1,2])
    def test_positive_2(self):
        """Позитивный на 2 параметра"""
        self.assertEqual(twoSum.Solution().twoSum([3,3], 6), [0,1])
    def test_no_int(self):
        """тип не int"""
        with self.assertRaises(ValueError) as e:
            twoSum.Solution().twoSum([2, 7, 11, 15], 9.2)
        self.assertEqual("Тип параметров должен быть int неотрицательным",e.exception.args[0])
    def test_negative (self):
        """отрицательные значения"""
        with self.assertRaises(ValueError) as e:
            twoSum.Solution().twoSum([-1], 2)
        self.assertEqual("Тип параметров должен быть int неотрицательным",e.exception.args[0])
    def test_no_list (self):
        """не список"""
        with self.assertRaises(ValueError) as e:
            twoSum.Solution().twoSum(4, 0)
        self.assertEqual("Первый параметр должен быть списком",e.exception.args[0])
if __name__=='__main__':
    main()