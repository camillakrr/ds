import socket
import os


PORT = 8800


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', PORT))
s.listen()
while True:
    conn, addr = s.accept()
    filename = conn.recv(1024).decode("utf-8")
    filename_list = filename.split('.')
    if filename in os.listdir():
        i = 1
        while True:
            filename = filename_list[0] + '_copy' + str(i) + '.' + filename_list[1]
            if filename in os.listdir():
                i += 1
            else:
                break
    else:
        filename = filename_list[0] + '.' + filename_list[1]
    fw = open(filename, "wb")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        else:
            fw.write(data)
    fw.close()
    print('Dowloading complete\nSaved: ' + filename)
    conn.close()
