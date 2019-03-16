import csv

names = list()

with open('names.txt', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        names = row

names.sort()


def name_score(n):
    s = 0
    for c in n:
        s += ord(c) - ord('A') + 1
    return s


# print(name_score("COLIN"))
s = 0
for i in range(len(names)):
    s += (i+1) * name_score(names[i])

print(s)  # 871198282
