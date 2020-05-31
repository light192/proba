with open("mac-address-table.txt", "r") as f:
    for line in f:
        if line[0] in "0123456789":
            elements = line.split()
            print("{:4}{:17}{}".format(elements[0], elements[1], elements[3]))
