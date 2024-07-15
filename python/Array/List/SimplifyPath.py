class Solution:
    def simplifyPath(self, path: str) -> str:
        loc=path.split('/')
        path=[]
        for i in loc:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if len(path) > 0:
                    path.pop()
            else:
                path.append(i)
        res=""
        for j in path:
            res+="/"+j
        return res if len(res) > 0 else "/"
            