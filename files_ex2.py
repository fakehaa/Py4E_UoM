# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
full = 0    
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    number = float(line.split(":")[1])
    total = number +total
    full = full +1
    #print(line)
average = total/full
    

print("Average spam confidence:", average)
