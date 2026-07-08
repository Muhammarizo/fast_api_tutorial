from ast import List


def has_duplicate(nums: List[int]) -> bool:
    my_set = set(nums)
    return len(my_set) != len(nums)


print(has_duplicate([1, 2, 3, 4, 5, 5]))
