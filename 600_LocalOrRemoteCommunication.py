#Given source IP, source subnet, and destination IP
#Print whether the communication will be Local or Remote

def address_dec_to_binary(ip_addr):
	bin_ip = ""
	for i in ip_addr.split("."):
		x = str(bin(int(i)))[2:]
		if len(x)<8:
			x = "0"*(8-len(x)) + x
		bin_ip += x + "."
	return bin_ip[:-1]

def perform_and( ip1 , ip2):
	ip1 = ip1.split(".")
	ip2 = ip2.split(".")
	anded = ""
	for i in range(4):
		anded+= str(bin(int(ip1[i]) & int(ip2[i])))[2:] + "."
	anded_final=""
	for i in anded[:-1].split("."):
		if len(i)<8:
			anded_final += "0"*(8-len(i)) + i + "."
		else:
			anded_final += i + "."

	return anded_final[:-1]

source_ip = input("\n\nEnter Source IP: ")
source_subnet = input("Enter the Source Subnet: ")
dest_ip = input("Enter Destination IP: ")

source_ip_binary = address_dec_to_binary(source_ip)
source_subnet_binary = address_dec_to_binary(source_subnet)
dest_ip_binary = address_dec_to_binary(dest_ip)

and_x = perform_and(source_ip , source_subnet)
and_y = perform_and(dest_ip , source_subnet)

print("\nSource IP Binary: " , source_ip_binary)
print("Source Subnet Binary: " , source_subnet_binary)
print("Destination IP Binary: " , dest_ip_binary)
print("--------------------------------------------------------")
print("Source IP AND Source Subnet: " , and_x)
print("Destination IP AND Source Subnet: " , and_y)
print("--------------------------------------------------------")
if and_x == and_y:
	print("LOCAL COMMUNICATION")
else:
	print("REMOTE COMMUNICATION")


