from collections import deque

def parse_csv(data):
    "Splits a string of comma-separated values into rows and columns."
    parsed_data = []
    rows = data.split("\n")
    for row in rows:
        columns = [col.strip() for col in row.split(",")]
        parsed_data.append(columns)

    return parsed_data


def unique_anagrams(words):
    "Counts how many unique anagram groups exist in a list of strings."
    seen_words = set()

    for word in words:
        seen_words.add("".join(sorted(word)))
    
    return len(seen_words)


def max_in_window(nums, k):
    if not nums or k == 0:
        return []

    result = []
    dq = deque()

    for i, num in enumerate(nums):
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result



# Design a simple URL shortener function shorten_url(url: str) -> str.
# Each unique URL should always map to the same shortened ID.
# Shortened IDs should be short strings (e.g., abc123).
# For simplicity, use an incrementing counter + base62 encoding (characters [a-zA-Z0-9]).

class UrlShortener:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.counter = 0
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def _encode(self, num):
        """Convert a number to base62 string."""
        if num == 0:
            return self.alphabet[0]
        chars = []
        base = len(self.alphabet)
        while num > 0:
            num, rem = divmod(num, base)
            chars.append(self.alphabet[rem])
        return "".join(reversed(chars))

    def shorten_url(self, url):
        if url in self.url_to_code:
            return self.url_to_code[url]
        code = self._encode(self.counter)
        self.counter += 1
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        return code

    def expand_url(self, code):
        return self.code_to_url.get(code)    

test_url = UrlShortener()
print(test_url.shorten_url("https://example.com"))
print(test_url.shorten_url("https://new.com"))
print(test_url.shorten_url("https://example.com"))
