l1 = ["Grapes", "Banana"]
l2 = [11,33,55,77,99]
l3 = [False, True, True, False]
l4 = [l1, l2, l3]

l5 = l4.copy()                                  #shallow copy
print("l5:", l5)
l5[2][2] = 100
print("l5:", l5)
print("l4:", l4)
print("l3:", l3)

l6 = [l1.copy(), l2.copy(), l3.copy()]          #deep copy
l6[1][2] = 1000
print("l2:", l2)
print("l4:", l4)
print("l6:", l6)