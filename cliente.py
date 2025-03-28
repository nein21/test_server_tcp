
import os
import socket
import logging

# Configurar logging
log_folder = "log"
log_file_path = os.path.join(log_folder, "client.log")
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

HOST = '127.0.0.1'
PORT = 5000

try:
    # Crear socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    logging.info(f"Conectado al servidor {HOST}:{PORT}")

    while True :

        # Enviar mensaje al servidor
        user_message = input("Por favor, introduce el mensaje: ")
        client_socket.sendall(user_message.encode('utf-8'))
        logging.info(f"Mensaje enviado al servidor: {user_message}")
        print(f"Mensaje enviado: {user_message}")

        # Recibir respuesta del servidor
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Respuesta Servidor: {data}")
        logging.info(f"Respuesta recibida del servidor: {data}")

        if str(user_message) == "DESCONEXION":
            break

except ConnectionRefusedError:
    logging.error("Error: No se pudo conectar al servidor.")
except Exception as e:
    logging.error(f"Error en la comunicación con el servidor: {e}")
finally:
    client_socket.close()
    print("Conexión cerrada")
    logging.info("Conexión cerrada")