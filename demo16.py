# for x in range(10):
#     print(x)

# for x in range(10, 50):
#     print(x)

for x in range(1, 100, 2):                  #printing all the odd numbers
    print(x)

l1 = [11,33,44,22,66,77,99,55,88,11,44,77,22,11]
d1 = {}
for x in l1:
   d1[x] = l1.index(x)

print(d1)

for keys in d1:
   print(keys, "=", d1[keys])

# l1 = [11,15,19]
# print(l1)
# print(*l1)

# s1, s2, s3 = l1
# print(s1)