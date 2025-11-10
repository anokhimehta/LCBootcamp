# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None

        if p.val == root.val or q.val == root.val:
            return root 
        left = self.lowestCommonAncestor(root.left, p ,q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        else:
            return left or right





class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                #heap is already size k
                heapq.heappushpop(heap, (val,key))

        return [h[1] for h in heap]
        
