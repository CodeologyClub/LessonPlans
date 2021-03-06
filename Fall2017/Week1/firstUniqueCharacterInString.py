# Given a string, find the first non-repeating character in it and return
# it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0
#
# s = "loveleetcode"
# return 2
#
# Note: you may assume the string contains only lowercase letters

def firstUniqChar(s):
    # create the frequency dict
    counts = {char: s.count(char) for char in s}

    # now find the first unique char
    for i, char in enumerate(s):
        if counts[char] == 1:
            return i

    # default
    return -1

def the_long_way(s):
    # create the frequency dict
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    # now find the first unique char
    for i in range(len(s)):
        char = s[i]
        if counts[char] == 1:
            return i

    # default
    return -1

def tests():
    s1 = "leetcode" #0
    s2 = "loveleetcode" #2
    s3 = "apple" #0
    s4 = "" #-1
    s5 = "aabbcc" #-1
    s6 = "aabbc" #4
    print(firstUniqChar(s1) == 0)
    print(firstUniqChar(s2) == 2)
    print(firstUniqChar(s3) == 0)
    print(firstUniqChar(s4) == -1)
    print(firstUniqChar(s5) == -1)
    print(firstUniqChar(s6) == 4)

tests()
