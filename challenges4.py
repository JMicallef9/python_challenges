import heapq
from collections import deque, defaultdict

def merge_sorted(num_lists):
    "Merges lists of numbers into a single, fully sorted list."

    for lst in num_lists:
        lst.sort()

    merged = []
    heap = []
    for index, lst in enumerate(num_lists):
        if lst:
            heapq.heappush(heap, (lst[0], index, 0))

    while heap:
        value, list_index, element_index = heapq.heappop(heap)
        merged.append(value)
        if element_index + 1 < len(num_lists[list_index]):
            heapq.heappush(heap, (num_lists[list_index][element_index+1], list_index, element_index+1))

    return merged


def is_balanced(string):
    "Checks that a string contains matching brackets, returns True or False."
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack


def execution_order(tasks):
    "Returns valid execution order for a list of tasks with dependencies."
    indegree = defaultdict(int)
    graph = defaultdict(list)

    for task, deps in tasks.items():
        indegree[task]
        for dep in deps:
            graph[dep].append(task)
            indegree[task] += 1
            indegree[dep]

    queue = deque([t for t in tasks if indegree[t] == 0])
    order = []

    while queue:
        curr = queue.popleft()
        order.append(curr)
        for neighbour in graph[curr]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    if len(order) != len(tasks):
        raise ValueError("Cyclic dependency detected")
    return order