import time
from binary_search_tree import BinarySearchTree
start_time = time.time()
import sys
sys.setrecursionlimit(10**6)


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()


f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:     # This is runtime O(n^2)
#         if name_1 == name_2:
#             duplicates.append(name_1)



# Rule Breaking solution that works


# ----------------------------------

# names1 = sorted(names_1)
# names2 = sorted(names_2)
# for i in range(0, len(names1)-1):
#     if names1[i] == names1[i+1]:

#         names1[i] = str(i*22)
# for i in range(0, len(names2)-1):
#     if names2[i] == names2[i+1]:

#         names2[i] = str(i*3.157)
# allname = sorted(names1 + names2)

# for i in range(0, len(allname)-1):
#     if allname[i] == allname[i+1]:
#         duplicates.append(allname[i])



# maple = BinarySearchTree("Mario Luigi")
# for name in names_3:
#     maple.insert(name)


# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

dupes = (set(names_1) & set(names_2))

for dupe in dupes:
    duplicates.append(dupe)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")