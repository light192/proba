adr = input("Введите IP-адрес и длину префикса (ip/mask): ")
ip = adr[:adr.find("/")]
pref = adr[adr.find("/"):]
mask = '1'*int(pref[1:])+'0'*(32-int(pref[1:]))
sm = [mask[:8],mask[8:16],mask[16:24],mask[24:]]
ip = ip.split(".")
ip[0] = int(ip[0]) & int(sm[0],2)
ip[1] = int(ip[1]) & int(sm[1],2)
ip[2] = int(ip[2]) & int(sm[2],2)
ip[3] = int(ip[3]) & int(sm[3],2)
print("Network:")
print (f"{ip[0]:<10}{ip[1]:<10}{ip[2]:<10}{ip[3]:<10}")
print (f"{int(ip[0]):08b}  {int(ip[1]):08b}  {int(ip[2]):08b}  {int(ip[3]):08b}")

print("\nMask:")
print(pref)
print(f"{int(sm[0],2):<10}{int(sm[1],2):<10}{int(sm[2],2):<10}{int(sm[3],2):<10}")
print(f"{sm[0]:10}{sm[1]:10}{sm[2]:10}{sm[3]:10}")
