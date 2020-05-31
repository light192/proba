access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

access = {
    '0/12': '10',
    '0/14': '11',
    '0/16': '17',
    '0/17': '150'
}
trunk = {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }

for intf, vlan in access.items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))

for intf, vlans in trunk.items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            if vlans[0] == 'add':
                vlans.remove("add")
                print(' {} add {}'.format(command, ",".join(vlans)))
            elif vlans[0] == 'del':
                vlans.remove("del")
                print(' {} remove {}'.format(command, ",".join(vlans)))
            elif vlans[0] == 'only':
                vlans.remove("only")
                print(' {} {}'.format(command, ",".join(vlans)))
        else:
            print(' {}'.format(command))
