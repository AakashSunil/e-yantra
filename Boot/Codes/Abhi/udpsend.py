import socket
import re

UDP_IP = "192.168.10.16"
UDP_PORT = 4210
MESSAGE = "AB"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message: ", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
