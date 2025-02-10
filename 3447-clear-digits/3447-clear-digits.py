class Solution:
    def clearDigits(self, s: str) -> str:

        letters = []
        for i in range(len(s)):
            if not s[i].isdigit():
                letters.append(s[i])
            elif letters:
                letters.pop()

        return ''.join(letters)

            
