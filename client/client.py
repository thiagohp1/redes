import socket

host = '192.168.0.184'
port_number = 8888

def get_html():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port_number))
    client_socket.sendall('GET / HTTP/1.1'.encode('utf-8'))
    data = client_socket.recv(1024)

    with open('index.html', 'wb') as file:
        file.write(data)

    print('HTML recebido e salvo como index.html')
    client_socket.close()

def get_jpg():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port_number))
    client_socket.sendall('GET /image.jpg HTTP/1.1'.encode('utf-8'))
    file = open('image.jpg', 'wb')
    data = client_socket.recv(1024)
    
    while data:
        file.write(data)
        data = client_socket.recv(1024)

    print('Imagem recebida e salva como image.jpg')
    client_socket.close()

if __name__ == "__main__":
    get_html()
    get_jpg()
