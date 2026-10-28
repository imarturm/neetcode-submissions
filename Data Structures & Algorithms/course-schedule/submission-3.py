from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        post = defaultdict(list)
        for course, prereq in prerequisites:
            indeg[course] += 1
            post[prereq].append(course)

        queue = deque(course for course in range(numCourses) if indeg[course] == 0)
        taken = 0
        while queue:
            course = queue.popleft()
            taken += 1
            for nxt in post[course]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    queue.append(nxt)
        return taken == numCourses