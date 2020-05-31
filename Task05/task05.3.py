mode = input("Введите режим интерфейса: ")
intf = input("Введите идентификатор интерфейса: ")
vlans = input("Введите номер влан(ов): ")

conf = {
        "access":
            "interface {}\n"
            "switchport mode access\n"
            "switchport access vlan {}\n"
            "switchport nonegotiate\n"
            "spanning-tree portfast\n"
            "spanning-tree bpduguard",
        "trunk":
            "interface {}\n"
            "switchport trunk encapsulation dot1q\n"
            "switchport mode trunk\n"
            "switchport trunk allowed vlan {}"
        }

print(conf[mode].format(intf, vlans))
