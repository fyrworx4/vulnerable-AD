with open('sorted.txt') as f:
    lines = f.readlines()

new = []

for i in range(len(lines)):
    new.append(lines[i].replace("\n",""))

print(new)