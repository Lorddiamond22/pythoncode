import socket

hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)
print("Nama komputer adalah " + hostname)
print("IP address saya adalah "+str(ipAddress))