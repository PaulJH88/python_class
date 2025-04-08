str1 = "I am \t'Himadrie' and \\ \nI live in \t\"Vadodara\""

print(str1.count("a"))
print(str1.find("mad"))
print(str1.islower())
print(str1.upper())
print(str1.lower())
print(str1.split("\""))

name = input("Please enter your name: ")
hobby = input("Please enter your hobby: ")
num = input("Please enter your fav num: ")

str1 = "We are happy to have {s_name} who have {s_hobby} as a hobby  and {s_fav_num} as their favourite number."
#Part 2
print(str1.format(s_name = name, s_hobby= hobby, s_fav_num=num))