class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        listS = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    ListS[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)
    
    test = "((f(oo))f)"
    minRemoveToMakeValid(self, test)