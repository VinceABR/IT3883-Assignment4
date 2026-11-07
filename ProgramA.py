
# Program Name: ProgramA.py
# Course: IT3883 / Section W01
# Student Name: Vince Abraham
# Assignment Number: 4
# Due Date: November 6th 11:59
# Purpose: Ask the user for a message, send it to a
# server, and display the uppercase response.

import socket

# Identify the server's IP address and port
server_ip = "127.0.0.1"
server_port = 45000

# Ask the user to enter a message
message = input("Enter a message: ")

# Create a TCP socket and connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((server_ip, server_port))

    # Send the message to Program B
    client.sendall(message.encode("utf-8"))

    # Receive and decode the server's response
    response = client.recv(1024).decode("utf-8")

    # Display the response
    print("Server response:", response)
