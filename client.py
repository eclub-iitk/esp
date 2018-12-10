import socket

UDP_IP_ADDRESS ="127.0.0.1"
UDP_PORT_NO = 6789

Message = "Hello,Server"
#Creating a socket
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    clientSock.sendto(Message.encode('utf-8'), (UDP_IP_ADDRESS,UDP_PORT_NO))
    #print("Sending")
clientSock.close()