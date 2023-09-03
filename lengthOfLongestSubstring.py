# условие задачи https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        lengthOfLongestSubstring возвращает длину самой длинной подстроки без повторяющихся символов

        :param s: строка
        :return: int длинна строки
        """
        if s == "": return 0
        max_str = s[0]
        temp_str = s[0]
        l = len(s)
        for i in range(1, l):
            if temp_str.find(s[i]) == -1:
                temp_str = temp_str + s[i]
            elif len(temp_str) > len(max_str):
                max_str = temp_str
                temp_str = s[i]
                j = i - 1
                while j >= 0:
                    if temp_str.find(s[j]) == -1:
                        temp_str = s[j] + temp_str
                    else:
                        break
                    j -= 1
            else:
                temp_str = s[i]
                j = i - 1
                while j >= 0:
                    if temp_str.find(s[j]) == -1:
                        temp_str = s[j] + temp_str
                    else:
                        break
                    j -= 1
        if len(temp_str) > len(max_str):
            return len(temp_str)
        else:
            return len(max_str)
