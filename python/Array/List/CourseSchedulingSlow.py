class Course:
    def __init__(self, code:int):
        self.code=code
        self.pre=set()
        self.after=set()

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        courses={}
        for p in prerequisites:
            if p[0] not in courses:
                courses[p[0]]=Course(p[0])
            if p[1] not in courses:
                courses[p[1]]=Course(p[1])
            courses[p[0]].pre.add(p[1])
            courses[p[1]].after.add(p[0])
        queue=deque()
        res=set()
        for code in courses.keys():
            if not courses[code].pre:
                res.add(code)
            else:
                queue.append(code)

        
        firstTime=True
        first=queue[0]
        size=len(queue)
        memo={}
        while queue:
            if len(queue) in memo:
                if queue[0] in memo[len(queue)]:
                    break
                else:
                    memo[len(queue)].add(queue[0])
            else:
                memo[len(queue)]=set([queue[0]])
            
            c=queue.popleft()
            passed=True
            for i in courses[c].pre:
                if i not in res:
                    passed=False
                    break
            if passed:
                res.add(c)
            else:
                queue.append(c)
        return len(courses.keys())==len(res)
    
    def canFinishThreeStates(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # three states approach
        def buildAdjacencyList(numCourses: int, pre: List[List[int]]) -> List[List[int]]:
            res=[[] for _ in range(numCourses)]
            for i in pre:
                res[i[0]].append(i[1])
            return res

        states=[0]*numCourses
        adjList=buildAdjacencyList(numCourses, prerequisites)

        def isCycle(course: int) -> bool:
            if states[course]==-1:
                return True
            if states[course]==1:
                return False
            states[course]=-1
            for i in adjList[course]:
                if isCycle(i):
                    return True
            
            states[course]=1
            return False

        for i in range(numCourses):
            if isCycle(i):
                return False
        return True
    
    def canFinishStack(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # three states approach
        def buildAdjacencyList(numCourses: int, pre: List[List[int]]) -> List[List[int]]:
            res=[[] for _ in range(numCourses)]
            for i in pre:
                res[i[0]].append(i[1])
            return res

        adjList=buildAdjacencyList(numCourses, prerequisites)
        visited=set()

        def isCycle(course: int, stack) -> bool:
            if course in visited:
                if course in stack:
                    return True
                return False
                
            stack.append(course)
            visited.add(course)

            for i in adjList[course]:
                if isCycle(i, stack):
                    return True
            
            stack.pop()
            return False

        for i in range(numCourses):
            if isCycle(i, []):
                return False
        return True

            



            

