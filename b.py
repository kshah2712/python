#Write a Python program to remove an item from a set if it is present in the set.
# 20CS018-Dev Halvawala

num_set = set([0, 1, 2, 3, 4, 5])
print("Original set elements:")
print(num_set)
print("Remove 4 from the said set:")
num_set.discard(4)
print(num_set)
print("Remove 5 from the said set:")
num_set.discard(5)
print(num_set)
print("Remove 2 from the said set:")
num_set.discard(2)
print(num_set)
