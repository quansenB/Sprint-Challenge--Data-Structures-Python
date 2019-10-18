import time
from bintrees import AVLTree

start_time = time.time()
names_1 = AVLTree()

f = open('names_1.txt', 'r')
for line in f:
    names_1.insert(line, None)
f.close()

duplicates = []

f = open('names_2.txt', 'r')
for line in f:
    if names_1.__contains__(line):
        duplicates.append(line)
f.close()


end_time = time.time()
print (f"\n{len(duplicates)} duplicates:\n\n{''.join(duplicates)}\n")
print (f"runtime: {end_time - start_time} seconds")

