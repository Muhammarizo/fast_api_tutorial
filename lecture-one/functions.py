def my_function(name):  # name is a parameter
    print("Hello", name)


my_function("Emil")  # "Emil" is an argument


def name(firstname,
         /):  # argumentlarni ohiriga / belgi qoyilsa faqat positional-only bolib qoladi. yani keyword yoza olmaymiz
    print("Hello", firstname)


# name(firstname = "rizo")  error
name("rizo")  # true


def name2(*, firstname, lastname):  # argumentlardan oldin * belgi qoyilsa keyword argument bolib qoladi
    print("Hello", firstname)


name2(firstname="s", lastname="s")


# Combining positional-only and kwyword-only
def name3(a, b, /, *, c, d):
    return a + b + c + d


result = name3(5, 10, c=15, d=20)
print(result)

name = "rizo"


def test():
    global name
    name = "abdu"
    print(name)


test()
print(name)
