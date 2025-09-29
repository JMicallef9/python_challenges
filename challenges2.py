from collections import defaultdict

def parse_config(config_list):
    """
    Ignores empty lines and lines starting with #.
    Splits valid lines into key/value pairs.
    Returns them as a dictionary.
    """
    config_dict = {}

    for item in config_list:
        if item.strip() and not item.lstrip().startswith("#"):
            key, value = item.split("=", 1)
            config_dict[key] = value
    
    return config_dict


def flatten(nested_list):
    "Flattens a list of arbitrarily nested lists."

    new_list = []
    for item in nested_list:
        if isinstance(item, list):
            new_list.extend(flatten(item))
        else:
            new_list.append(item)
    return new_list



log_list = ["[2025-09-24 10:23:11] GET /api/users 200",
            "[2025-09-24 10:23:12] POST /api/login 403",
            "[2025-09-24 10:23:14] GET /api/users 200"]

def count_status_codes(logs):
    log_dict = defaultdict(int)

    for log in logs:
        log_dict[int(log.split(" ")[-1])] += 1
    
    return dict(log_dict)


# Regex version:

# import re
# from collections import defaultdict

# def count_status_codes(logs):
#     log_dict = defaultdict(int)
#     pattern = re.compile(r"\s(\d{3})$")  # matches the 3-digit status at end
#     for log in logs:
#         match = pattern.search(log)
#         if match:
#             log_dict[int(match.group(1))] += 1
#     return dict(log_dict)



jobs = [
    (1, 4),
    (2, 5),
    (7, 8),
    (3, 6),
    (5, 7)
]

def max_non_overlapping(jobs):
    jobs.sort(key=lambda x: x[1])  # sort by end time
    count = 0
    last_end = float('-inf')
    for start, end in jobs:
        if start >= last_end:
            count += 1
            last_end = end
    return count