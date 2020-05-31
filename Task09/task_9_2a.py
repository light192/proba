trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    '''
    intf_trunk_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/1': [10, 20, 30],
         'FastEthernet0/2': [11, 30],
         'FastEthernet0/4': [17]}
    trunk_template - список команд для порта в режиме trunk
    '''
    result = {}
    for intf, vlans in intf_vlan_mapping.items():
        commands = []
        for command in trunk_template:
            if "allowed vlan" in command:
                vlans_str = ""
                for vlan in vlans:
                    vlans_str += str(vlan) + ","
                commands.append("{} {}".format(command, vlans_str[:-1]))
            else:
                commands.append(command)
        result[intf] = commands
    return result

print(generate_trunk_config(trunk_config, trunk_mode_template))







'''

 'interface FastEthernet0/12',
'switchport mode access',
'switchport access vlan 10',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
'interface FastEthernet0/17',
'switchport mode access',
'switchport access vlan 150',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
...]
'''
