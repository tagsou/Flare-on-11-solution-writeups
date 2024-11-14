import socket
import os

# Server Configuration
HOST = '127.0.0.1'
PORT = 1337
BUFFER_SIZE = 4096

# Example values for key, nonce, and file path
KEY = bytes.fromhex('8dec9112eb760eda7c7d87a443271c35d9e0cb878993b4d904aef934fa2166d7')
NONCE = bytes.fromhex('111111111111111111111111')
FILE_PATH = "/root/certificate_authority_signing_key.txt"  # Update this with an actual file path

def send_data(client_socket):
    try:
        # Step 1: Send the 32-byte key
        client_socket.sendall(KEY)
        print(f"Sent Key: {KEY.hex()}")

        # Step 2: Send the 12-byte nonce
        client_socket.sendall(NONCE)
        print(f"Sent Nonce: {NONCE.hex()}")

        # Step 3: Send 4 bytes representing the file path length
        file_path_encoded = FILE_PATH.encode('utf-8')
        file_path_size = len(file_path_encoded)
        file_path_size_bytes = file_path_size.to_bytes(4, byteorder='little')
        client_socket.sendall(file_path_size_bytes)
        print(f"Sent File Path Size: {file_path_size}")

        # Step 4: Send the actual file path
        client_socket.sendall(file_path_encoded)
        print(f"Sent File Path: {FILE_PATH}")

        # Step 5: Wait to receive the file size and processed file content from the client
        received_file_size_data = client_socket.recv(4)
        received_file_size = int.from_bytes(received_file_size_data, byteorder='little')
        print(f"Received File Size: {received_file_size}")

        received_file_content = b''
        while len(received_file_content) < received_file_size:
            part = client_socket.recv(BUFFER_SIZE)
            if not part:
                break
            received_file_content += part

        print(f"Received File Content: {received_file_content}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def main():
    # Create a socket and bind to the specified HOST and PORT
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Listening on {HOST}:{PORT}")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            send_data(client_socket)
    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
