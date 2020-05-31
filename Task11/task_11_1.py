def parse_cdp_neighbors(command_output):
    lines = command_output.split("\n")
    start = False
    items = ""
    result = {}
    for line in lines:
        if ">" in line:
            hostname = line.split(">")[0]
        if "#" in line:
            hostname = line.split(">")[0]
        if start and line != "":
            items = line.split()
            result[(hostname, items[1]+items[2])] = (items[0], items[-2]+items[-1])
        if line.startswith("Device"):
            start = True
    return result


f = open("sh_cdp_n_sw1.txt", "r")
lines = f.read()
print(parse_cdp_neighbors(lines))
