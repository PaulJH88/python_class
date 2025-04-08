Demo3.py

#Part 1
tool = input("Please enter your favourite tool: ")
print(tool, " has ", len(tool), " letters.")

#part 2
fav_num = int(input("Please enter your fav num: "))

if fav_num%2 == 0:
    print(fav_num, " is even")
else:
    print(fav_num," is odd")

#part 3
hobbies = input("Please enter your hobbies, seperated by a comma: ")
print("Hobbies: ", hobbies.split(","))
Trial3.py


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