import twoSum
import lengthOfLongestSubstring

if __name__ == '__main__':

    nums = [2, 7, 11, 15]
    target = 9
    print("[0,1] = ",end='')
    print(twoSum.Solution().twoSum(nums, target))

    s = "abcabcbb"
    print("3 = ",end='')
    print(lengthOfLongestSubstring.Solution().lengthOfLongestSubstring(s))


