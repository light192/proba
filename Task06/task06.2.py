ip_addr = input("Введите ip-адрес: ")
ip = ip_addr.split(".")

if int(ip[0]) > 0 and int(ip[0]) <=223:
    print("unicast")
elif int(ip[0]) > 223 and int(ip[0]) <= 239:
    print("multicast")
elif ip_addr == "255.255.255.255":
    print("local broadcast")
elif ip_addr == "0.0.0.0":
    print("unassigned")
else:
    print("unused")
