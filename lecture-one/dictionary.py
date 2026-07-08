"""
Dictionary
"""

# user_dictionary = {"username": "codingwithrizo", "name": "Muhammadrizo", "age": 27, 23: "45", "aa": "aa"}
#
# print(user_dictionary)
# print(len(user_dictionary))
#
# user_dictionary.pop("age")
# print(user_dictionary)
#
# user_dictionary.clear()
# print(user_dictionary)

# del user_dictionary
# print(user_dictionary)


# dictionaryni loop qilganda faqat keylarini beradi
admin_dictionary = {"username": "codingwithrizo", "name": "Muhammadrizo", "age": 27, }

# add new value or update
admin_dictionary["role"] = "teacher" # bu yerda role degan key yoq bolgani uchun dicitionary ohiriga shu malumot qoshiladi
admin_dictionary["role"] = "HR" # bu yerda role degan key allaqachon mavjud. Shuning uchun update boladi
for key in admin_dictionary:
    print(key)

# agar loop jarayonida value ham kerak bolsa quyidagicha yozamiz
for key, value in admin_dictionary.items():
    print(key, value)


# dictionaryni boshqa bir ozgaruvchiga copy qilishimiz ham mumkin
admin_dictionary2 = admin_dictionary
admin_dictionary2.pop("age")
print(admin_dictionary)
# bu yerda admin_dictionary dan ham malumot ochgan boladi. Sababi biz shunchaki xotiradagi malumotga ikkita nom berdik
# bu nafaqat dictionary da balki list da ham shunaqa

admin_dictionary2 = admin_dictionary.copy() # copy ishlatilinsa hotirada alohida joy ajratiladi
admin_dictionary2.pop("name")
print(admin_dictionary)






