with open("mac-address-table.txt", "r") as f:
    lines = f.readlines()
lines.sort()
new_lines = []
for line in lines:
    if line[0] in "0123456789":
        elements = line.split()
        elements[0] = int(elements[0])
        new_lines.append(elements)

new_lines.sort()

vlan = int(input("Введите номер VLAN: "))

#print(new_lines)
for line in new_lines:
    if line[0] == vlan:
        print("{:<7}{:<17}{}".format(line[0], line[1], line[3]))
