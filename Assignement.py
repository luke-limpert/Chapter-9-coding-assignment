name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
words = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith("From ") : continue
    words = line.split()
    counts[words[1]] = counts.get(words[1], 0) + 1

Highest = None
Popular = None

for Sender,count in counts.items():
    if Highest is None or count > Popular:
        Highest = Sender
        Popular = count

print(Highest, Popular)
