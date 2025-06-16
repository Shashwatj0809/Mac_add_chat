import socket
import threading

# Load allowed MAC addresses
with open("allowed.txt", "r") as f:
    allowed_macs = [line.strip().replace("-", ":").lower() for line in f.readlines()]

# List to keep track of connected clients
clients = []

def broadcast(message, current_client):
    for client in clients:
        if client != current_client:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            break
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 12345))  # Listen on all interfaces
    server.listen(5)
    print("[*] Server started on port 12345...")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] New connection from {addr}")

        # Receive MAC address from client
        try:
            client_mac = client_socket.recv(1024).decode().strip().replace("-", ":").lower()
            print(f"Client {addr[0]} sent MAC {client_mac}")

            if client_mac in allowed_macs:
                client_socket.send("Access Granted".encode())
                clients.append(client_socket)
                thread = threading.Thread(target=handle_client, args=(client_socket,))
                thread.start()
            else:
                client_socket.send("Access Denied. Your MAC is not allowed.".encode())
                client_socket.close()
        except Exception as e:
            print(f"[!] Error handling client {addr}: {e}")
            client_socket.close()

if __name__ == "__main__":
    main()
