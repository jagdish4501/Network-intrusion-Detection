import socket

def get_local_ip():
    # Get the hostname of the local machine
    hostname = socket.gethostname()

    # Get the IP addresses associated with the hostname
    ip_addresses = socket.getaddrinfo(hostname, None)

    # Extract IPv4 and IPv6 addresses
    ipv4_addresses = [addr[4][0] for addr in ip_addresses if addr[0] == socket.AF_INET]
    ipv6_addresses = [addr[4][0] for addr in ip_addresses if addr[0] == socket.AF_INET6]

    return [ipv6_addresses, ipv4_addresses]

[ipv4_addresses, ipv6_addresses] = get_local_ip()
print("IPv4 Addresses:", ipv4_addresses)
print("IPv6 Addresses:", ipv6_addresses)
