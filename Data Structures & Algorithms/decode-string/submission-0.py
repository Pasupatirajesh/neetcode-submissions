class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        current_num = ""
        for c in s:
            if c.isnumeric():
                current_num+=c
            elif c == '[':
                stack.append((current_str, int(current_num)))
                current_str = ""
                current_num = ""
            elif c == ']':
                last_string , multiplier = stack.pop()
                current_str = last_string + (current_str * multiplier)
            else:
                current_str+=c
        return current_str
