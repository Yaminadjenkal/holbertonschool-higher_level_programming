import socket
import json

def start_server():
    host = 'localhost'
    port = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            if data:
                received_dict = json.loads(data.decode('utf-8'))
                print("Received Dictionary from Client:")
                print(received_dict)

def send_data(dictionary):
    host = 'localhost'
    port = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        serialized_data = json.dumps(dictionary).encode('utf-8')
        client_socket.sendall(serialized_data)

if __name__ == "__main__":
    import threading
    import time

    def main():
        # Start the server in a separate thread
        server_thread = threading.Thread(target=start_server)
        server_thread.start()

        # Give server some time to start listening
        time.sleep(1)

        # Run the client to send data
        sample_dict = {
            'name': 'Alice',
            'age': 30,
            'city': 'Paris'
        }
        send_data(sample_dict)

        # Ensure server thread ends
        server_thread.join()

    main()
