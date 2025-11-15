
######RIGHT VIEW OF TREE

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        #root always visible 

        # for each level we want the right most node
        # do level by level traversal

        res = []
        queue = collections.deque([root])
        cur = root

        while (queue):
            #get num items in queue, should be num nodes at a level
            qlen = len(queue) 
            right = None 

            #sets right to right most node in the level
            for i in range(qlen):
                node = queue.popleft()
                if (node):
                    right = node
                    queue.append(right.left)
                    queue.append(right.right)
            if right:
                res.append(right.val)

        return res


#####ROTTING ORANGES

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        #we can maintain queue of rotten oranges
        #for each orange in queue we run bfs
        #need tracker/count for minutes
        #need tracker/count for fresh oranges

        q = deque()
        time = 0
        fresh = 0

        rows, cols = len(grid), len(grid[0])

        #make tally of fresh oranges and track rotten orange indices
        for i in range(rows):
            for j in range(cols):
                #count fresh
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i,j])

        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        while q and fresh > 0:

            #pop each rotten orange in q
            for i in range(len(q)):
                r, c = q.popleft()
                #iterate through all 4 directions relative to r,c
                for x,y in directions:
                    row, col = r+x, c+y
                    #check if in bounds and if fresh
                    if (row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or 
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1



#####COURSE SELECTION

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #for each node need to build adjacency list
        prereq = {c:[] for c in range(numCourses)}
        #each course index has list of prereqs
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visited = set()
        cycle = set()

        def dfs(crs):
            #detected cycle
            if crs in cycle:
                return False
            #dont need to visit twice
            if crs in visited:
                return True

            #recursively run dfs
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False

            #if we reach here no cycles
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output
        




        

        

        
