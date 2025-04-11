#Writing
# f = open("Example.txt", "w")
# f.write("THis is an example file. \nWe are trying file handling in Python.\nHave a good day!")
# f.close()

#appending
f = open("Example.txt", "a")
f.write("\nThis is an example of appending the data to the file.\n\nSuccessful!")
f.close()

#Reading
f = open("Example.txt", "r")
lines = f.read(15)
lines = f.read()
lines = f.readline()
print(lines)
lines = f.readline()
print(lines)

lines = f.readline()
print(lines)