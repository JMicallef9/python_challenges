import heapq

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