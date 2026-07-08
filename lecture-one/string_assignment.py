days = input("How many days until your birhtday: ")
approxWeek = int(days) // 7
print(f"{approxWeek} number of weeks until your birthday")

# -------------------------- Solution2
days = int(input("How many days until your birthday: "))  # input ni int wrapperga urash orqali inputdan kelayotgan value ni avto parse qilsak boladi. raqam kiritilmasa error beradi

print(round(days / 7, 2)) # round wrapper bizga verguldan keyin nechta aniqlikda korsatishni aytadi

