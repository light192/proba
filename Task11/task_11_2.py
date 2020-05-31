from draw_network_graph import draw_topology

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
            a = (hostname, items[1]+items[2])
            b = (items[0], items[-2]+items[-1])
            if items[0] < hostname:
                a, b = b, a
            result[a] = b
        if line.startswith("Device"):
            start = True
    return result

def create_network_map(filenames):
    links = {}
    for file in filenames:
        f = open(file, "r")
        lines = f.read()
        links.update(parse_cdp_neighbors(lines))
    return links

files = ["sh_cdp_n_sw1.txt","sh_cdp_n_r1.txt", "sh_cdp_n_r2.txt", "sh_cdp_n_r3.txt"]
print(create_network_map(files))
draw_topology(create_network_map(files))
