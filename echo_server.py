#! /usr/bin/env python
"""
Author:
    Christian P. Byrne
Course:
    CSC346 | Fall 21
Usage:
    echo_server.py port

Replies back to client exactly what was sent.
Can talk to multiple clients at once because it
is multithreaded.

'every time that you accept() a new socket, I want 
you to do all of the send()s and recv()s for that 
socket on another thread.'


"""

import sys
from socket import *
import threading


class ChatSocket:
    def __init__(self, sock, num):
        """Class for socket that indefinitely echoes req content.

        Args:
            sock        :   socket object.
            num (int)   :   Identifier in server.


        """
        self.sock = sock
        self.num = num
        self.END_TAG = "&END;"
        self.echo()

    def terminate(self):
        """Close socket.
        """
        self.sock.close()
        self.sock = False

    def _send(self, msg):
        """Send encoded string down socket.
        """
        self.sock.sendall((msg + self.END_TAG + "\r\n").encode())
        print("\nMessage Echoed", f"to Client {self.num}")

    def echo(self):
        """Indefinitely read and echo buffer contents until socket shutdown.
        """
        while self.sock:
            res = self.sock.recv(1024)
            if not res or res.decode() == "\r\n":
                break
            self._send(res.decode())
        print(f"Client {self.num} has left the chat.")


def main():
    port = int(sys.argv[1])
    server_sock = socket()
    server_sock.bind(("0.0.0.0", port))
    server_sock.listen(5)
    print(f"Server bind on 0.0.0.0:{port}")

    client_num = 1
    while True:
        (conn_sock, _) = server_sock.accept()
        threading.Thread(target=ChatSocket, args=(
            conn_sock, client_num)).start()
        client_num += 1


if __name__ == "__main__":
    main()
