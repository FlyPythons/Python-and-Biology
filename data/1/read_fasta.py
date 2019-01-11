# read the sequence file to python

for line in open("ampR.fasta"):
    line = line.strip()

    # starts with '>'
    if line.startswith(">"):
        name, description = line[1:].split(" ", maxsplit=1)
        seq = ""
    else:
        seq += line

print("name: %s\ndescription: %s\nseq: %s" % (name, description, seq))

# length
print("length: %s" % len(seq))

# ATCG
a = seq.count("A")
t = seq.count("T")
c = seq.count("C")
g = seq.count("G")
print("A: %s\nT: %s\nC: %s\nG: %s" % (a, t, c, g))

# GC %
print("GC%%: %s" % ((g+c)*100.0/len(seq)))
