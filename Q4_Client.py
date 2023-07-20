import socket

def main():
    host = '192.168.243.128'
    port = 8888

    # Create socket 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server
        client_socket.connect((host, port))
        print(f"Connected to {host} on port {port}")

        # Send/receive data server
        message = "@_@"
        client_socket.sendall(message.encode())

        # Receive data from server
        response = client_socket.recv(1024).decode()
        print("Received from server:", response)

    except socket.error as e:
        print(f"Error: {e}")
    finally:
        # Close socket 
        client_socket.close()

if __name__ == "__main__":
    main()

