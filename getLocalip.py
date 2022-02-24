import socket

b=socket.getfqdn()
hostname = socket.gethostname()
ip=socket.gethostbyname(hostname)
print("\nHostname :",hostname)
print("IP is :",ip)
print("")




