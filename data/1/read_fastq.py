# read the sequence file to python
n = 0

for line in open("ampR.fastq"):
    line = line.strip()
    if not line:
        continue
    n += 1
    # starts with '@'
    if line.startswith("@") and n != 4:
        name = line[1:].split(" ", maxsplit=1)[0]
        seq = score = ""
        n = 1
    elif n == 2:
        seq = line
    elif n == 3:
        assert line.startswith("+"), "error fastq record"
    elif n == 4:
        score = line
    else:
        pass

print("name: %s\nseq: %s" % (name, seq))

# length
print("length: %s" % len(seq))

# score
phred33 = [ord(i)-33 for i in score]
print("score: %s\nPhred33: %s" % (score, phred33))

