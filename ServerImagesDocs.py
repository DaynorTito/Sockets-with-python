import socket
import os

def handle_request(client_socket):
    request = client_socket.recv(1024).decode()
    print(f"Solicitud recibida: {request}")

    # Extraer el nombre del archivo solicitado de la solicitud HTTP
    filename = request.split()[1][1:]

    # Determinar el tipo MIME del archivo solicitado
    if filename.endswith('.pdf'):
        content_type = 'application/pdf'
    elif filename.endswith(('.jpg', '.jpeg')):
        content_type = 'image/jpeg'
    elif filename.endswith('.png'):
        content_type = 'image/png'
    else:
        error_message = "Tipo de archivo no admitido."
        client_socket.send("HTTP/1.1 404 Not Found\n\n".encode() + error_message.encode())
        client_socket.close()
        return

    try:
        with open(filename, 'rb') as file:
            content = file.read()
            header = f"HTTP/1.1 200 OK\nContent-Type: {content_type}\n\n"
            client_socket.send(header.encode() + content)
    except FileNotFoundError:
        error_message = "Archivo no encontrado."
        client_socket.send("HTTP/1.1 404 Not Found\n\n".encode() + error_message.encode())
    client_socket.close()

def main():
    host = '127.0.0.1'
    port = 8088

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Servidor web en {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Cliente conectado desde {client_address}")
        handle_request(client_socket)

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Cliente conectado desde {client_address}")
        handle_request(client_socket)

if __name__ == "__main__":
    main()
