import heapq

def merge_sorted(num_lists):
    "Merges lists of numbers into a single, fully sorted list."
    merged = []
    heap = []
    for i, lst in enumerate(num_lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
            print(heap)

    while heap:
        val, li, ei = heapq.heappop(heap)
        merged.append(val)
        if ei + 1 < len(num_lists[li]):
            heapq.heappush(heap, (num_lists[li][ei+1], li, ei+1))

    return merged


lists = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
print(merge_sorted(lists))

# # Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_balanced(string):
    "Checks that a string contains matching brackets, returns True or False."
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack


def execution_order(tasks):
    "Returns valid execution order for a list of tasks with dependencies."
    pass


# tasks = {
#     "compile": ["generate_code"],
#     "generate_code": ["fetch_schemas"],
#     "fetch_schemas": [],
#     "test": ["compile"]
# }

# execution_order(tasks)
# # Output (one valid order):
# ["fetch_schemas", "generate_code", "compile", "test"]