#! /usr/bin/env python
"""
Author:
    Christian P. Byrne
Course:
    CSC346 | Fall 21
Usage:
    pythone3 one_to_one.py host port

'like telnet, but even simpler'

 - Connects
 - Sends a single line of input
 - Reads any responses
 - Terminates

"""


import sys
from socket import *


def main():
    """Connect to server socket, send a message read from stdin, 
    read and display response then close socket and quit.
    """
    host, port = sys.argv[1:]
    sock = socket()
    sock.connect((host, int(port)))
    print(f"Connected to {host}:{port} as client.")

    print("\nEnter Message:")
    sock.sendall((input() + "\r\n").encode())
    print("\nMessage Sent to", host)

    def p_buffer(s): return s.recv(1024)
    res_concat = ""
    while len(p_buffer(sock)) > 16:
        # Continue reading buffer while greater than closing tag byte size
        res_concat += p_buffer(sock).decode()
    print(res_concat)
    sock.close()


if __name__ == "__main__":
    main()
