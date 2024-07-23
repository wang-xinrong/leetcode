class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def buildAdjacencyList(numCourses:int, pre:List[List[int]]) -> List[List[int]]:
            res=[[] for _ in range(numCourses)]
            for e in pre:
                res[e[1]].append(e[0])
            return res

        adjList=buildAdjacencyList(numCourses, prerequisites)
        inDegrees=[0]*numCourses
        for i in prerequisites:
            inDegrees[i[0]]+=1

        queue=deque([])
        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)

        res=[]

        while queue:
            temp=queue.popleft()
            res.append(temp)
            for i in adjList[temp]:
                inDegrees[i]-=1
                if inDegrees[i]==0:
                    queue.append(i)
            
        if len(res)==numCourses:
            return res
        else:
            return []

