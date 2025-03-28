from src.controller.server_controller import ServerController

if __name__ == "__main__":
    server = ServerController(host="0.0.0.0", port=5000)
    server.start_server()