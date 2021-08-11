class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical_path = path.split("/")
        stack = []
        for i in canonical_path:
            if i=="..":
                if stack:
                    stack.pop()
            elif i=="." or not i:
                continue
            else:
                stack.append(i)
        canonical_path = "/" + "/".join(stack)
        return canonical_path