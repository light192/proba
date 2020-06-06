'''
Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов
Для проверки доступности IP-адреса, используйте ping.
'''
import subprocess
import ipaddress
import os
import tabulate

def convert_ranges_to_ip_list(ip_list):
    result = []
    for item in ip_list:
        ips = item.split("-")
        if len(ips) == 2:
            start = ips[0].split(".")
            finish = ips[1].split(".")
            for i in range(int(start[-1]), int(finish[-1]) + 1):
                start[3] = str(i)
                ip = ".".join(start)
                result.append(ip)
        else:
            result.append(ips[0])
    return result

def ping_ip_addresses(ip_list):
    ip_list = convert_ranges_to_ip_list(ip_list)
    avail_ip = []
    unavail_ip = []
    for ip in ip_list:
        result = subprocess.run(["ping", ip, "-c", "3"], stdout = subprocess.PIPE)
        if result.returncode == 0:
            avail_ip.append(ip)
        else:
            unavail_ip.append(ip)
    return avail_ip, unavail_ip

def print_ip_table(av_ip_list, unav_ip_list):
    max = len(av_ip_list)
    if len(unav_ip_list) > max:
        for i in range(len(unav_ip_list) - len(av_ip_list)):
            print(i)
            av_ip_list.append("")
    else:
        for i in range(len(av_ip_list) - len(unav_ip_list)):
            print(i)
            unav_ip_list.append("")
    print(avail_ip)
    print(unavail_ip)
    ips = list(zip(avail_ip, unavail_ip))
    print(ips)
    cols = ["Reachable", "Unreachable"]
    print(tabulate.tabulate(ips, headers=cols))


avail_ip, unavail_ip = ping_ip_addresses(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132'])
a = print_ip_table(avail_ip, unavail_ip)
#print(list(a))
