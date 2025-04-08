list1 = [1,2,3,4]
lista = ['a','b','c','d']
shallow_list1a = [list1, lista]

print("Original list")
print(list1)
print(lista)
print(shallow_list1a)
print()

shallow_list1a[0][1] = -2

print("Altered shallow list")
print(list1)
print(lista)
print(shallow_list1a)
print()

deep_list1a = [list1.copy(), lista.copy()]

print("Original deep list")
print(list1)
print(lista)
print(deep_list1a)
print()

deep_list1a[0][1] = 22

print("Altered deep list")
print(list1)
print(lista)
print(deep_list1a)