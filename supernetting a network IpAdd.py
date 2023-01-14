import ipaddress

# input the IP address range and subnet mask
start_ip = input("Enter the starting IP address: ")
end_ip = input("Enter the ending IP address: ")
subnet_mask = input("Enter the subnet mask: ")

# convert the input to IP address objects
start_ip = ipaddress.IPv4Address(start_ip)
end_ip = ipaddress.IPv4Address(end_ip)
subnet_mask = ipaddress.IPv4Address(subnet_mask)

# create a supernet
supernet = ipaddress.supernet_of(ipaddress.summarize_address_range(start_ip, end_ip), subnet_mask)

# print the supernet
print("Supernet:", supernet)
