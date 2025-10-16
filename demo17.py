s_names = ["James", "Jimmy", "Bob", "Trevor", "Donald", "Washington", "Jim", "Joe"]
print(s_names)

sorted_names = sorted(s_names)
print(sorted_names)

reverse_names = sorted(s_names, reverse=True)
print(reverse_names)

len_names = sorted(s_names, key=len)
print(len_names)

rev_len_names = sorted(s_names, key=len, reverse=True)
print(rev_len_names)

s_names = []

while True:
    name = input("Please enter a name: ")
    s_names.append(name)

    res = input("Do you want to continue? Y/N ")
    if res == "N":
        break
    
print(s_names)
sorted_names = sorted(s_names)
print(sorted_names)

reverse_names = sorted(s_names, reverse=True)
print(reverse_names)

len_names = sorted(s_names, key=len)
print(len_names)

rev_len_names = sorted(s_names, key=len, reverse=True)
print(rev_len_names)