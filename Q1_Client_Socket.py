import socket
import requests

def main():
    host = 'izani.synology.me'
    port = 8443

    # UiTM Student ID
    student_id = '2022815738'

    try:
        # socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect server
        client_socket.connect((host, port))
        print(f"Connected to {host} on port {port}")

        # Send UiTM Student ID 
        client_socket.sendall(student_id.encode())

        # server response 
        response = client_socket.recv(1024).decode()
        print("Received from server:", response)

        # response contains the unique URL
        unique_url = response.strip()  

        # Close socket
        client_socket.close()

        # Access the unique URL 
        response = requests.get(unique_url)
        print("Next instructions:")
        print(response.text)

    except (socket.error, requests.RequestException) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
