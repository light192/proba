with open('ospf.txt') as f:
    for line in f:
        item = line.split()
        res_str = [
            "Protocol:               OSPF",
            "Prefix:                 {}",
            "AD/Metric:              {}",
            "Next-Hop:               {}",
            "Last update:            {}",
            "Outbound Interface:     {}"
        ]
        print("\n".join(res_str).format(item[1], item[2].strip("[]"), item[4].strip(","),
            item[5].strip(","), item[6]))
