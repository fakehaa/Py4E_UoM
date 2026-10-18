name = input("Enter file:")

most = dict()

if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = 0

for line in handle:
    word = line.split()
    if len(word) < 2 or word[0] != 'From':
        continue
    hour = word[5].split(':')[0]
    most[hour] = most.get(hour, 0) + 1
#print(most)

#print(most.items())

sorted_items = sorted(most.items())

#print(sorted_items) 


for k,v in sorted_items:
    print(k,v)