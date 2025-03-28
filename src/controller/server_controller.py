# app/controller.py

import socket
from src.model.messaje_model import Message
from src.view.message_view import MessageView

class ServerController:
    def __init__(self, host="0.0.0.0", port=5000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = None
        self.addr = None

    def start_server(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            MessageView.show_message(f"Servidor TCP iniciado en {self.host}:{self.port}")

            while True:
                self.conn, self.addr = self.server_socket.accept()
                MessageView.show_message(f"Conexión recibida de {self.addr}")
                try:
                    while True:
                        data = self.conn.recv(1024).decode('utf-8')
                        if not data:
                            MessageView.show_message("Cliente envió datos vacíos")
                            self.conn.sendall("Cliente envió datos vacíos".encode('utf-8'))
                            self.conn.close()
                            continue

                        # Procesar mensaje
                        message = Message(data)
                        response = message.process()

                        # Enviar respuesta al cliente
                        self.conn.sendall(response.encode('utf-8'))
                        MessageView.show_message(f"Respuesta enviada a {self.addr}: {response}")
                        if str(message) == "DESCONEXION":
                            break
                except Exception as e:
                    MessageView.show_error(f"Error con {self.addr}: {e}")

                finally:
                    self.close_connection()

        except Exception as e:
            MessageView.show_error(f"Error en el servidor: {e}")

        finally:
            self.server_socket.close()
            MessageView.show_message("Servidor detenido")


    def close_connection(self):
        self.conn.sendall(f"Conexión cerrada con {self.addr}".encode('utf-8'))
        self.conn.close()
        MessageView.show_message(f"Conexión cerrada con {self.addr}")
