class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            is_palindrome = True
            length = len(s)
            for i in range(length // 2):
                if s[i] != s[length - i - 1]:
                    is_palindrome = False
                    break
            if is_palindrome:
                return s
        return ""
