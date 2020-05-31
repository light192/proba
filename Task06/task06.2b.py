while True:
    ip_addr = input("Введите ip-адрес: ")
    ip = ip_addr.split(".")
    ip_correct = True
    if len(ip) == 4:
        for each in ip:
            each = int(each)
            if each < 0 or each > 255:
                print ("Неправильный ip-адрес")
                ip_correct = False
    else:
        print ("Неправильный ip-адрес")
        ip_correct = False
    if ip_correct:
        break
if ip_correct:
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
