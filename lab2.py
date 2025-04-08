#Part 1
s_name = "Vrajesh"
s_hobby = "Cooking"
s_fav_num = 7

#Part 2
print("We are happy to have ",s_name, " who have ",s_hobby," as a hobby  and ",s_fav_num," as their favourite number.")

#part 3
ages = [34, 29, 30, 31]
sum = 0

for age in ages:
    sum += age

print("Total ages: ",sum)
average = sum/len(ages)
print("The average age here is: ",average)

#part 4
no_of_eggs = 12
rem = no_of_eggs%s_fav_num
print("After Vrajesh took ",s_fav_num," eggs from the box , we have ",rem, " remaining in the box")