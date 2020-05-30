from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

with open(argv[1], "r") as f:
    for line in f:
        ignore.append("!")
        check = True
        for ignore_str in ignore:
            if ignore_str in line.strip():
                check = False
        if check:
            print(line.strip("\n"))
