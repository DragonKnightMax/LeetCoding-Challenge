class Solution:
    def reverseWords(self, s: str) -> str:
        reverse_words = s.split()[::-1]
        return " ".join(reverse_words)
