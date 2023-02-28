import socket

with open('hostnames.txt', 'r') as fh:
    urls = fh.readlines()

urls = [url.strip() for url in urls]  # strip `\n`

i = 1

for url in urls:
    hostname = url
    ip = ""
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        print(i, "Hostname:", hostname, '-->> No se puede resolver la IP')
        pass
    else:
        print(i, 'Hostname:', hostname,  'IP:', ip)
    i=i+1
