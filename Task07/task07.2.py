from sys import argv

with open(argv[1], "r") as f:
    for line in f:
        if line.strip() != "!":
            print(line.strip("\n"))
