import socket

def convert_to_atmosphere(pressure):
    
    return pressure * 0.986923

def main():
    host = '192.168.243.128'
    port = 8443

    # Create socket 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket 
    server_socket.bind((host, port))

    # Listening
    server_socket.listen(1)
    print("Server listening on {}:{}".format(host, port))

    while True:
        # Accept client 
        client_socket, client_addr = server_socket.accept()
        print("Connection established with {}".format(client_addr))

        # Receive pressure value 
        pressure = client_socket.recv(1024).decode()
        pressure = float(pressure)

        # Convert pressure 
        atmosphere_standard = convert_to_atmosphere(pressure)

        # Send the converted value 
        client_socket.sendall(str(atmosphere_standard).encode())

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    main()
