# Program Name: ProgramB.py
# Course: IT3883 / Section W01
# Student Name: Vince Abraham
# Assignment Number: 4
# Due Date: November 6th 11:59
# Purpose: Receive a message through a network socket,
# convert the message to uppercase, and return it.

import socket

# Set the server's address and port
server_ip = "127.0.0.1"
server_port = 45000

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((server_ip, server_port))
    server.listen(1)

    print("Server is waiting for a connection...")

    # Accept an incoming connection
    connection, address = server.accept()

    with connection:
        print("Connected to:", address)

        # Receive and decode the client's message
        message = connection.recv(1024).decode("utf-8")
        print("Received:", message)

        # Convert the message to uppercase
        uppercase_message = message.upper()

        # Send the converted message back
        connection.sendall(uppercase_message.encode("utf-8"))
        print("Sent back:", uppercase_message)
