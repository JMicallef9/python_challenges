from collections import defaultdict

def summarize_logs(log_list):
    """
    Counts each occurrence of a log level in a list of log lines.
    e.g. input = [
    "2025-09-24 12:05:33 INFO User 123 logged in",
    "2025-09-24 12:07:10 ERROR User 456 failed authentication",
    "2025-09-24 12:09:55 INFO User 123 logged out"
    ]
    Expected output = {
    "INFO": 2,
    "ERROR": 1
    }
    """
    log_dict = defaultdict(int)

    for line in log_list:
        log_level = line.split()[2]
        log_dict[log_level] += 1
    
    return dict(log_dict)


def group_users(users):
    """
    Receives a dictionary in the following format:
    users = [
    {"id": 1, "name": "Alice", "groups": ["admin", "dev"]},
    {"id": 2, "name": "Bob", "groups": ["dev"]},
    {"id": 3, "name": "Charlie", "groups": []}
    ]
    And returns a dictionary in which each group maps to a list of user names.
    """
    user_dict = defaultdict(list)
    for user in users:
        for group in user["groups"]:
            user_dict[group].append(user["name"])
    
    return dict(user_dict)


def find_missing(nums):
    "Finds the smallest positive integer not present in a list."

    nums_set = set(nums)

    smallest_int = 1

    while smallest_int in nums_set:
        smallest_int += 1
    
    return smallest_int

