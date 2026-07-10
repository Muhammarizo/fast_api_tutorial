def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    dict1 = {}
    dict2 = {}

    for char in s:
        dict1[char] = dict1.get(char, 0) + 1
    for char in t:
        dict2[char] = dict2.get(char, 0) + 1
    print(dict1)
    print(dict2)

    for char in s:
        if dict1[char] != dict2.get(char):
            return False
    return  True


s = "jar"

t = "jam"

print(is_anagram(s, t))
