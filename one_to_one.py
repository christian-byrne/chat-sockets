#! /usr/bin/env python
"""
Author:
    Christian P. Byrne
Course:
    CSC346 | Fall 21
Usage:
    pythone3 one_to_one.py host port

"the most dumb of chat applications." A single server talking to
a single client. Does not support multiple clients at once. 

A client and server in the same file. If the hostname arg is 
'server', act as server.


"""

import sys
from socket import *


class ChatSocket:
    def __init__(self, sock, server=False):
        """Class for single-threaded chat sockets.

        Args:
            sock :          socket object.
            server (bool) : Whether server socket or not.


        """
        self.sock = sock
        self.server = server
        self.EXIT_CODE = "&TERMINATE;"
        self.END_TAG = "&END;"

    def _send(self):
        """Send encoded string down socket.
        """
        print("\nEnter Message:")
        msg = input()
        self.sock.sendall(
            (msg + self.END_TAG if msg else self.EXIT_CODE + "\r\n").encode()
        )
        print("\nMessage Sent\n")

        return False if not msg else True

    def _receive(self):
        """Read buffer until empty and print decoded result to stdout.
        """
        def uni_buffer(): return self.sock.recv(1024).decode()
        print("Awaiting message. . .")

        data = buffer = uni_buffer()
        while self.END_TAG not in buffer and self.EXIT_CODE not in buffer:
            buffer = uni_buffer()[:]
            data += buffer

        print(
            "\nMessage Received:\n"
            + data.replace(self.END_TAG, "")
        )

        return False if self.EXIT_CODE in data else True

    def terminate(self):
        """Close socket.
        """
        self.sock.close()
        self.sock = False

    def trade_messages(self):
        """Alternate between sending a message and receiving a message
        until exit code from either socket.
        """
        try:
            if not self.server:
                self._send()
            while self.sock:
                if not self._receive():
                    print(
                        "Client has left the chat\n"
                        + "Awaiting new connections. . .\n"
                    )
                    break
                if not self._send():
                    break

        except KeyboardInterrupt:
            self.terminate()
            return


def client(host, port):
    """Create client socket and start trading messages until exit code.
    """
    sock = socket()
    sock.connect((host, port))
    print(f"Connected to {host}:{port} as client.")

    sock = ChatSocket(sock)
    sock.trade_messages()
    sock.terminate()


def server(port):
    """Create server socket, start listening, accept each connection 
    sequentially and start trading messages until exit code, then 
    accept next connection.


    """
    server_sock = socket()
    server_sock.bind(("0.0.0.0", port))
    print(f"Server bind on 0.0.0.0:{port}")
    server_sock.listen(5)

    while True:
        (conn_sock, _) = server_sock.accept()
        conn_sock = ChatSocket(conn_sock, True)
        conn_sock.trade_messages()


def main():
    host, port = sys.argv[1:]
    if host == "server":
        server(int(port))
    else:
        client(host, int(port))


if __name__ == "__main__":
    main()
