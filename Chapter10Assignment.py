name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
hours = list()


for line in handle:
    line = line.rstrip()
    if not line.startswith("From ") : continue
    line = line.split()
    time = line[5]
    hours = time.split(":")
    counts[hours[0]] = counts.get(hours[0],0) + 1

finish = sorted([ (k,v) for k,v in counts.items() ])
for hour, val in finish:
    print(hour, val)
