import time
from binary_search_tree import BinarySearchTree #pylint: disable=import-error

          #Original Code

#start_time = time.time()

#f = open('names_1.txt', 'r')
#names_1 = f.read().split("\n")  # List containing 10000 names
#f.close()

#f = open('names_2.txt', 'r')
#names_2 = f.read().split("\n")  # List containing 10000 names
#f.close()

#duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
#bst = BinarySearchTree()
#for name_1 in names_1:
    #for name_2 in names_2:
        #if name_1 == name_2:
            #duplicates.append(name_1)

#for name_2 in names_2:
    #if bst.contains(name_2):
        #duplicates.append(name_2)

#end_time = time.time()
#print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
#print (f"runtime: {end_time - start_time} seconds")


#Pre-op code
    #TC: O(n^2)
    #RT: 4.734 seconds

#Post-OP code:
    #*added Binary Search Tree
    #RTC: 0.0109 seconds

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


#Optimizing further with Python's built in 'Set' tools for data structures. (Hash table rather than tree)
#Resource: https://www.geeksforgeeks.org/sets-in-python/


# TC: 0(n)
# RT: 0.00698 seconds!!!

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n") #Opens first list with 1k names! Splits it up!
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n") #Opens second list with 1k names! and Split it up!
f.close()

duplicates = [] #Return our sets of duplicates in this list here

#Use the set function to populate the duplicate list from set(file)s
duplicates = list(set(names_1) & set(names_2))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")