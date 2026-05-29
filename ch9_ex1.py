
name = input("Enter file:")
most = dict()
name_list = list()

if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = 0

for line in handle:
    line = line.rstrip()
    word = line.split()

    if len(word) < 1:
        continue
    if word[0] != 'From':
        continue
    name_list.append(word[1])

for name in name_list:
    most[name] = most.get(name, 0) + 1

bigcount = None
bigword = None

for name, count in most.items():
    if bigcount is None or count > bigcount:
        bigword = name
        bigcount =  count

print(bigword, bigcount)