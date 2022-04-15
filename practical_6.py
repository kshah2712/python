# You are given n words. Some words may repeat. For each word, output its
# number of occurrences. The output order should correspond with the input order
# of appearance of the word. See the sample input/output for clarification.
# Sample Input
# 4
# bcdef
# abcdefg
# bcde
# bcdef
# 20CS018-Dev Halvawala

N = int(input())
dict = {}
list = []

for i in range(N):
  k = input()
  list.append(k)
  if k in dict:
    dict[k] += 1
  else:
    dict[k] = 1
    
print(len(dict))
print(' '.join([str(dict[k]) for k in dict]))