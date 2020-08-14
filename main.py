import socket

page_request = input("Enter URL (without http): ")

while len(page_request) < 1:
    page_request = input("Please write a valid URL: ")

connect_url = page_request.replace("www.","")
start_connection = True

while start_connection:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((connect_url, 80))
    cmd = 'GET {page_request} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')
    mysock.close()
    start_connection = False