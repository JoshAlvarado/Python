class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        slist = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    slist[i] = ''
        while stack:
            slist[stack.pop()] = ''
        return ''.join(slist)