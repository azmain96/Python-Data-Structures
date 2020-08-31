# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence: 0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
value = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    value += float(line[20:])
    count += 1

print('Average spam confidence:', value / count)


# OUTPUT
# Enter file name: mbox-short.txt
# Average spam confidence: 0.7507185185185187
