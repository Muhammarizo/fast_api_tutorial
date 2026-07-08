"""
Sets are similar to lists but are unordered and cannot contain duplications
Use curly brackets instead of []
"""

my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)
print(len(my_set)) # duplicate lar tushib qoladi

for x in my_set:
    print(x)


my_set.discard(3)
print(my_set) # 3 ga teng element tushib qoladi

# my_set.clear()
# print(my_set) # bu set dagi barcha elementlarni olib tashlaydi

my_set.add(3) # add methodi set ga yangi element qoshadi
print(my_set)

my_set.update([5,6,7]) # bir vaqtni ozida setga bir nechta element qoshish uchun iterable qilib qoshiladi
print(my_set)



"""
Tuples are ordered like lists but they are unchangeable, immutable
Use parentheses instead of []
"""

my_tuple = (1, 2, 3)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[1])

# we cannot change, add, remove or update tuples.
my_tuple[1] = 100; # we get an error




