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

# Used to be O(n^2)

maple = BinarySearchTree("Jean Velazquez") # She was first in line, so she gets to be the root.

for name in names_1: # Build a tree out of all the folks in list 1
    maple.insert(name)

for name in names_2: # Check for each of the list 2 folks in the tree.
                     # If we spot 'em, they get appended to the duplicate list!
    if maple.contains(name):
        duplicates.append(name)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

dupes = (set(names_1) & set(names_2))

for dupe in dupes:
    duplicates.append(dupe)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")