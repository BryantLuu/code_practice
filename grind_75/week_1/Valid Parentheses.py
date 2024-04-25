class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif not stack:
                return False
            else:
                open_bracket = stack.pop()
                if pairs[open_bracket] != char:
                    return False
        if not stack:
            return True
        return False