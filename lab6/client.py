import socket
import sys
import os


FILE = sys.argv[1]
HOST = sys.argv[2]
PORT = int(sys.argv[3])


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
f = open(FILE, 'rb')
s.send(bytes(FILE, 'utf-8'))
i = 1
while True:
    data = f.read(1024)
    print('Sending... ' + str(min(round(i * 1024 * 100 / os.path.getsize(FILE), 2), 100)) + '%')
    s.send(data)
    i += 1
    if not data:
        print('Successfully sent ' + FILE)
        break
f.close()
s.close()
