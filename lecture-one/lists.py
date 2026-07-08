""" Lists are a collection of data"""
my_list = [80, 12, 45, 66, 90]
print(my_list[2])

names = ["Rizo", "Rustam", "Abdu"]
print(names[-1])
print(len(names))

print(names[0:2]) # bu yerda range boyicha olish mumkin. yani 0 dan boshla va ikkigacha (2 kirmaydi)

names.append("Rapikjonov") # listni ohiriga yangi item qoshadi
print(names)

names.insert(1, "Abdulloh") # bu 1-indexga yani item qoshadi. Qolganlari onga suriladi. yani eski 1- item uchmadi
print(names)


names.remove("Abdu") # bu listdagi aynan shunga tegishli birinchi kelgan elementni ochiradi
print(names)


names.pop(1) # bu aynan specific (maxsus) indexga tegishli itemni olib tashlaydi by default -1 boladi yani ohirgi elementni olib tashlaydi
print(names)


names.sort() # bu yerda name larni alphabetic qilib sortlab beradi
print(names)


