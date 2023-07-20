import socket
import threading
import random

# Quotes
quotes = [
    "When in doubt, don't.",
    "Be truthful, nature only sides with truth.",
    "The other night I ate at a real nice family restaurant. Every table had an argument going.",
    "Do not let the bad make you doubt the good.",
    "The true color of one person is not determined by skin, but by the behavior in it.",
    "The only way to do great work is to love what you do.",
    "Turn your wounds into wisdom.",
    "Life is a succession of lessons which must be lived to be understood.",
	
]

def handle_client(client_socket):
    # Retrieve quote
    random_quote = random.choice(quotes)

    # Send the quote 
    client_socket.send(random_quote.encode())

    # Close the connection
    client_socket.close()

def main():
    host = '192.168.243.128'
    port = 8888

    # Create socket 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket
    server_socket.bind((host, port))

    # Listening
    server_socket.listen(5)
    print("Quote of the Day server listening on {}:{}".format(host, port))

    while True:
        # Accept connection
        client_socket, client_addr = server_socket.accept()
        print("Connection established with {}".format(client_addr))

        # Create a new thread 
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
