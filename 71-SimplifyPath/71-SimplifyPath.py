# Last updated: 5/16/2026, 12:30:17 PM
class Solution:

    def simplifyPath(self, path):
        path = path.split('/')
        stack = []
        for i in path:
            if i == '..':
                if len(stack):
                    stack.pop()
            elif i != '.' and i != '':
                stack.append(i)
        return '/' + '/'.join(stack)
# Method 2 =======================================================
    # def simplifyPath(self, path: str) -> str:
    #     parts = path.split('/')

    #     stack = []

    #     for part in parts:
    #         if part == '' or part == '.':
    #             continue
    #         if part == '..':
    #             if stack:
    #                 stack.pop()
    #             continue
            
    #         stack.append(part)

        
    #     res = ''
    #     while stack:
    #         res = '/' + stack.pop() + res
        
    #     return res if res else '/'



# Method 1 =======================================================
# one char by one char
    # def simplifyPath(self, path: str) -> str:
        
    #     fname = []
    #     stack = []
    #     for i in range(len(path)):
    #         char = path[i]

    #         if char != '/':
    #             fname.append(char)

    #         if char == '/' or i == len(path)-1:
    #             fstr = ''.join(fname)
    #             fname = []
    #             if len(fstr) == 0:
    #                 continue
                
    #             if fstr == '..':
    #                 if stack:
    #                     stack.pop()
    #                 continue
                    
    #             if fstr == '.':
    #                 continue

    #             stack.append(fstr)
                

    #     if len(stack) == 0:
    #         return '/'
    #     else:
    #         out = ''
    #         for item in stack:
    #             out += '/' + str(item)


    #         return out
            