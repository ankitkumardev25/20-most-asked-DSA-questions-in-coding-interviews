"""
18. Course Schedule (Cycle Detection in Directed Graph)
There are numCourses courses labeled 0 to numCourses-1.
Given prerequisites[i] = [ai, bi] meaning you must take course bi first to
take course ai, return true if you can finish all courses.

Example:
    Input: numCourses = 2, prerequisites = [[1, 0]]
    Output: True

    Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
    Output: False (cycle detected)

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from collections import defaultdict, deque


def can_finish(num_courses, prerequisites):
    # Topological sort (BFS / Kahn's algorithm)
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1

    queue = deque(c for c in range(num_courses) if in_degree[c] == 0)
    completed = 0

    while queue:
        course = queue.popleft()
        completed += 1
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return completed == num_courses


if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))           # True
    print(can_finish(2, [[1, 0], [0, 1]]))   # False
    print(can_finish(4, [[1, 0], [2, 1], [3, 2]]))  # True
