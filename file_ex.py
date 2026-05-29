fname = input("Enter the file name: ")
fh = open(fname)

for x in fh:
    x =x.rstrip()
    print(x.upper())