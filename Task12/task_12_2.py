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
        result = subprocess.run(["ping", ip, "-c", "3"])
        if result.returncode == 0:
            avail_ip.append(ip)
        else:
            unavail_ip.append(ip)
    return avail_ip, unavail_ip

avail_ip, unavail_ip = ping_ip_addresses(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132'])
print(avail_ip)
print(unavail_ip)
