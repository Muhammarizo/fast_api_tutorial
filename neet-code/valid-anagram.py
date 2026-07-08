class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        first_set = set(s)
        second_set = set(t)
        return len(first_set) == len(second_set)

print(Solution().is_anagram("dog", "cat"))