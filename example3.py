# Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.

# Use romeo.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lst, lst2 = [],[]
for line in fh:
  lst += line.split()
lst.sort()
for word in lst:
   if word in lst2: continue
   lst2.append(word)

print(lst2)


# OUTPUT:
#
# Enter file name: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
