import sys

for line in sys.stdin:
    line = line.strip()
    temperature = int(line[87:92])
    quality = int(line[92])
    if ((temperature != 9999) and (quality == (0 or 1 or 4 or 5 or 9))):
        print('%s\t%d' % (line[15:23], int(line[87:92])))