import socket
import sys
 
# hostname = sys.argv[1]

hostname = "ESTRELLA_DE_LA_MUERTE"

ip = socket.gethostbyname(hostname)
 
print('Hostname: ', hostname, '\n' 'IP: ', ip)
