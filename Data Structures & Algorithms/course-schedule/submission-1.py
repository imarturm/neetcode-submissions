from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        post = defaultdict(list)
        for p in prerequisites:
            pre[p[0]].append(p[1])
            post[p[1]].append(p[0])
        
        first_courses = [num for num in range(numCourses) if num not in pre]
        queue = deque(first_courses)
        visited = set(first_courses)
        while queue:
            course = queue.popleft()
            for post_course in post[course]:
                if post_course not in visited and all(prereq in visited for prereq in pre[post_course]):
                    queue.append(post_course)
                    visited.add(post_course)
        
        return len(visited) == numCourses