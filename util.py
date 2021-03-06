import socket


def recv_all(sock: socket.socket):
    output = bytes()
    while True:
        recvd = sock.recv(2048)
        output += recvd
        if len(recvd) < 2048:
            break

    return output
