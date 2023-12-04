import socket
import datetime
import threading

host = '192.168.0.184'
port_number = 8888

def generate_html(client_address):
    html_template = """<!DOCTYPE html>
    <html>
    <head>
        <title>Imagem</title>
    </head>
    <body>
        <h1>Imagem</h1>
        <img src="image.jpg" alt="Image">
        <p>Número da Porta: {port_number}</p>
        <p>IP do Cliente: {client_ip}</p>
    </body>
    </html>"""

    return html_template.format(port_number=client_address[1], client_ip=client_address[0])

def send_html(client_socket, client_address):
    html_content = generate_html(client_address)
    client_socket.sendall(html_content.encode('utf-8'))

def send_jpg(client_socket):
    with open('image.jpg', 'rb') as file:
        jpg_content = file.read()
        client_socket.sendall(jpg_content)

def log_connection(client_address):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{current_time}] Conexão apartir do Host: {socket.gethostname()} IP do cliente: {client_address[0]} Porta: {client_address[1]}\n"
    with open('server_log.txt', 'a') as log_file:
        log_file.write(log_message)

def handle_client(client_socket):
    client_address = client_socket.getpeername()
    log_connection(client_address)
    print(f"Conexão aceita de {client_address}")

    request = client_socket.recv(1024).decode('utf-8')

    if request == 'GET / HTTP/1.1':
        send_html(client_socket, client_address)
    elif request == 'GET /image.jpg HTTP/1.1':
        send_jpg(client_socket)

    client_socket.close()

def handle_connections():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port_number))
    server_socket.listen(5)

    print("Servidor aguardando conexão...")

    while True:
        client_socket, _ = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    handle_connections()
