import math
import os
import random
import re
import sys




def isValid(s):
    """
    Understand the requirement: a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times.
    
    Thoughts:
    1. how to make sure we have same occurrences of characters, and just one more. -- build a hashmap to see if there're only two sets and their occurrences only diff in 1.
    """
    from collections import defaultdict
    # 1. index characters
    counter = defaultdict(int)
    for i in s:
        counter[i] += 1
    # 2. index occurrences
    occurrences = defaultdict(set)
    for char in counter.keys():
        occurrences[counter[char]].add(char)
    # 3. judge
    if len(occurrences) >= 3:  # too much, only allow diff in 1
        return "NO"
    if len(occurrences) == 1:  # perfect
        return "YES"
    # We only could decrease one key, so that should be the larger key or an other one-lengthy char.
    if len(occurrences) == 2:
        max_key, min_key = max(occurrences.keys()), min(occurrences.keys())
        if (max_key - min_key) == 1 and len(occurrences[max_key]) == 1:
            return "YES"
        if len(occurrences[min_key]) == 1 and min_key == 1:
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
