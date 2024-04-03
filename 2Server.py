# Un servidor TCP que devuelva la fecha y hora a peticiones de clientes. 
import socket
import datetime

def main():
    # Configuración del servidor
    host = 'localhost'  # Dirección IP del servidor (localhost)
    port = 9876         # Puerto en el que escuchará el servidor

    # Crear un socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Vincular el socket al host y puerto
        server_socket.bind((host, port))

        # Escuchar conexiones entrantes (máximo 1 cliente en cola)
        server_socket.listen(1)
        print(f"Servidor escuchando en {host}:{port}")

        while True:
            # Aceptar una conexión entrante
            client_socket, client_address = server_socket.accept()
            print(f"Cliente conectado desde {client_address}")

            # Obtener la fecha y hora actual
            now = datetime.datetime.now()
            fecha_hora = now.strftime("%Y-%m-%d %H:%M:%S")

            # Enviar la fecha y hora al cliente
            client_socket.send(fecha_hora.encode())

            # Cerrar la conexión con el cliente
            client_socket.close()

    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario.")
    finally:
        # Cerrar el socket del servidor
        server_socket.close()

if __name__ == "__main__":
    main()
