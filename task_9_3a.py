
def get_int_vlan_map(config_filename):
    '''
      filename - имя файла конфигурации коммутатора
      На выходе - два кортежа:
      Первый - конфигурация портов доступа вида:
        {'FastEthernet0/12': 10,
         'FastEthernet0/14': 11,
         'FastEthernet0/16': 17}
      Второй - конфигурация транковых портов вида:
        {'FastEthernet0/1': [100, 200],
         'FastEthernet0/3': [100, 300, 400, 500, 600],
         'FastEthernet1/2': [400, 500, 600]}
    '''
    f = open(config_filename, 'r')
    config = f.read().split("\n")
    #print(config)
    access_config = {}
    trunk_config = {}
    for command in config:
        if command.startswith("interface"):
            intf = command[10:]
        if "access" in command:
            vlan = 1
            if "vlan" in command:
                vlan = int(command[command.find('vlan')+5:])
            access_config[intf] = vlan
        if "trunk allowed vlan" in command:
            vlans_str = command[command.find('vlan')+5:].split(',')
            vlans = []
            for vlan in vlans_str:
                vlans.append(int(vlan))
            trunk_config[intf] = vlans
    return access_config, trunk_config


access_config, trunk_config = get_int_vlan_map('config_sw2.txt')
print(access_config)
print(trunk_config)
