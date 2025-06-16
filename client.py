import socket
import threading
import uuid

def get_mac_address():
    # Get MAC in colon-separated lowercase format
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff)
                   for i in range(40, -1, -8)])
    return mac

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "Access Denied. Your MAC is not allowed.":
                print(message)
                client.close()
                break
            print(message)
        except:
            print("[!] Disconnected from server.")
            client.close()
            break

def main():
    server_ip = input("Enter server IP: ")
    port = 12345
    mac_address = get_mac_address()

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_ip, port))
        client.send(mac_address.encode())  # Send MAC address first

        response = client.recv(1024).decode()
        if "Access Denied" in response:
            print(response)
            client.close()
            return
        else:
            print(response)
            print("[*] Connected to chat. Type messages and press enter to send.")
        
        # Start thread to receive messages
        threading.Thread(target=receive_messages, args=(client,)).start()

        # Main thread sends messages
        while True:
            msg = input()
            client.send(msg.encode())

    except Exception as e:
        print(f"Failed to connect: {e}")

if __name__ == "__main__":
    main()
