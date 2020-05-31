adr = input("Введите IP-адрес и длину префикса (ip/mask): ")
ip = adr[:adr.find("/")]
pref = adr[adr.find("/"):]
ip = ip.split(".")
print("Network:")
print (f"{ip[0]:10}{ip[1]:10}{ip[2]:10}{ip[3]:10}")
print (f"{int(ip[0]):08b}  {int(ip[1]):08b}  {int(ip[2]):08b}  {int(ip[3]):08b}")

print("\nMask:")
print(pref)
mask = '1'*int(pref[1:])+'0'*(32-int(pref[1:]))
print(f"{int(mask[:8],2):<10}{int(mask[8:16],2):<10}{int(mask[16:24],2):<10}{int(mask[24:],2):<10}")
print(f"{mask[:8]:10}{mask[8:16]:10}{mask[16:24]:10}{mask[24:]:10}")
