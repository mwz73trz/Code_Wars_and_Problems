# The method calculate_mode will take an List of numbers or strings as its input and return an List of the most frequent values.

# For example:

# calculate_mode([1,2,3,3])         # => [3]
# calculate_mode([4.5, 0, 0])       # => [0]
# calculate_mode([1.5, -1, 1, 1.5]) # => [1.5]
# calculate_mode([1,1,2,2])         # => [1,2]
# calculate_mode([1,2,3])           # => [1,2,3], because all occur with equal frequency
# calculate_mode(["who", "what", "where", "who"]) # => ["who"]

from collections import Counter

def calculate_mode(arr):
    c = Counter(arr)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]

print(calculate_mode([1,2,3,3]))
print(calculate_mode([4.5, 0, 0]))
print(calculate_mode([1.5, -1, 1, 1.5]))
print(calculate_mode([1, 1, 2, 2]))
print(calculate_mode([1,2,3]))
print(calculate_mode(["who", "what", "where", "who"]))