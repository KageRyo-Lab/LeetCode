class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_x = reversed(str(x))
        return str(x) == ''.join(reverse_x) # 使用 ''.join() 將 reversed 出現的字符物件連接並轉換回字串