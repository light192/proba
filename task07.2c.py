from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

with open(argv[1], "r") as f_in, open (argv[2], "w") as f_out:
    for line in f_in:
        #ignore.append("!")
        check = True
        for ignore_str in ignore:
            if ignore_str in line.strip():
                check = False
        if check:
            f_out.write(line)
