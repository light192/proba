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

def ping_ip_addresses(ip_list):
    avail_ip = []
    unavail_ip = []
    for ip in ip_list:
        result = subprocess.run(["ping", ip, "-c", "3"])
        if result.returncode == 0:
            avail_ip.append(ip)
        else:
            unavail_ip.append(ip)
    return avail_ip, unavail_ip

avail_ip, unavail_ip = ping_ip_addresses(["192.168.0.68", "192.168.0.66"])
print(avail_ip)
print(unavail_ip)
