# Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
#20CS018-Dev Halvawala

def most_frequent(list):
    return max(set(list), key = list.count)
 
list = [20, 10, 30, 20, 10, 30, 30]
print(most_frequent(list))
