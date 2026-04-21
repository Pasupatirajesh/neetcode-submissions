# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            rightside = None
            qlen = len(q)
            for i in range(qlen):
                curr = q.popleft()
                if curr:
                    rightside = curr
                    q.append(curr.left)
                    q.append(curr.right)
            if rightside:
                res.append(rightside.val)
        return res 
        