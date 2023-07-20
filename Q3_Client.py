import socket

def main():
    host = '192.168.243.128'
    port = 8443

    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    client_socket.connect((host, port))

    # User input
    pressure = input("Enter pressure in bar: ")
    pressure = float(pressure)

    # Send pressure value 
    client_socket.sendall(str(pressure).encode())

    # Receive converted value 
    atmosphere_standard = client_socket.recv(1024).decode()

    # Display value
    print("Pressure in atmosphere standard: {}".format(atmosphere_standard))

    # Close connection
    client_socket.close()

if __name__ == "__main__":
    main()
