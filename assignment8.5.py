fname = input("Enter file name: ")
fh = open(fname)
count = 0
for un in fh:
    if un.startswith("From "):
        un = un.split()
        count = count + 1
        print(un[1])
         
print("There were", count, "lines in the file with From as the first word")