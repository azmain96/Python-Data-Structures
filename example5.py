# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Use the file name mbox-short.txt as the file name.
name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
counts = dict()
emails = list()
for all in handle:
    if not all.startswith('From:'): continue
    emails.append(all.split()[1])

for each in emails:
    counts[each] = counts.get(each, 0) + 1
mail = 0
count = 0

for key, val in counts.items():
    if val > count:
        mail = key
        count = val

print(mail, count)


# OUTPUT:

# Enter file:mbox-short.txt
# cwen@iupui.edu 5
