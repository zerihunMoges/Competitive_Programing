class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        bracket_pair = {')':'(','}': '{', ']':'['}
        is_valid = True
        for i in s:
            if i in bracket_pair.values():
                brackets.append(i)
            elif brackets == [] or brackets[-1] != bracket_pair[i]:
                return False
            elif brackets[-1] == bracket_pair[i]:
                brackets.pop()

        if len(brackets)  != 0:
            is_valid = False
        return is_valid
