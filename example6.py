# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# Use the file name mbox-short.txt as the file name.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = dict()
date = sorted(list([(line.split()[5])[0:2] for line in handle if line.startswith('From') and not line.startswith('From:')]))

for hour in date:
    hours[hour] = hours.get(hour, 0)+1

for key, val in hours.items():
    print(key, val)


# OUTPUT:

# Enter file:mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
