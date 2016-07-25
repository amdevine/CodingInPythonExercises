gccontent = []

s = open("sequences.txt")

for seq in s.readlines():
    gccount = 0
    for base in seq:
        if base == 'G' or base == 'C':
            gccount += 1
    gccontent.append(gccount/len(seq))

s.close()

print("Highest GC content: " + str(max(gccontent)))
