# Se quiere un programa que reciba como argumento una lista de nombres de sitios en Internet, por cada elemento de la lista su programa deberá retornar su dirección IP
import socket
import sys

def get_ip_address(domain):
    try:
        # Obtener la dirección IP del dominio
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def main():
    # Verificar si se proporcionaron nombres de dominio como argumentos en la línea de comandos
    if len(sys.argv) < 2:
        print("Obtener_direcciones_ip.py <dominio1> <dominio2> ...")
        sys.exit(1)
    # Obtener los nombres de dominio de los argumentos en la línea de comandos
    nombres_dominio = sys.argv[1:]

    # Obtener las direcciones IP para cada dominio
    for dominio in nombres_dominio:
        direccion_ip = get_ip_address(dominio)
        if direccion_ip:
            print(f"La dirección IP de {dominio} es {direccion_ip}")
        else:
            print(f"No se pudo resolver la dirección IP para {dominio}")

if __name__ == "__main__":
    main()
