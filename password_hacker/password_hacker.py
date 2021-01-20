import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("hostname")
parser.add_argument("port")
parser.add_argument("password")

args = parser.parse_args()

with socket.socket() as client_socket:
    address = (args.hostname, int(args.port))
    client_socket.connect(address)

    pswrd = args.password.encode()

    client_socket.send(pswrd)

    response = client_socket.recv(1024)
    response = response.decode()

    print(response)

