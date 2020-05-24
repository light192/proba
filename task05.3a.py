ask_vlan = {
    "access" : "Введите номер VLAN: ",
    "trunk"  : "Введите разрешенные VLANы: "
}
mode = input("Введите режим интерфейса: ")
intf = input("Введите идентификатор интерфейса: ")
vlans = input(ask_vlan[mode])

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

conf = {
        "access":
            "\n".join(access_template),
        "trunk":
            "\n".join(trunk_template)
        }

print(("interface {}\n"+conf[mode]).format(intf, vlans))
