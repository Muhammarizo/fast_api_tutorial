my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i = 0
while i < 3:
    i += 1
    for x in my_list:
        if x == "Monday":
            print("--------------------")
            continue
        print(x)
