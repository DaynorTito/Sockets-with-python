import socket

def main():
    # Configuración del cliente
    host = '127.0.0.1'  # Dirección IP del servidor (localhost)
    port = 9876         # Puerto en el que está escuchando el servidor

    # Crear un socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar al servidor
        client_socket.connect((host, port))

        # Recibir la fecha y hora del servidor
        fecha_hora = client_socket.recv(1024).decode()
        print(f"Fecha y hora del servidor: {fecha_hora}")

    except ConnectionRefusedError:
        print("No se pudo conectar al servidor. Asegúrate de que el servidor esté en funcionamiento.")
    finally:
        # Cerrar el socket del cliente
        client_socket.close()

if __name__ == "__main__":
    main()
