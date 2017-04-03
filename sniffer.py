import socket,os
host="10.0.0.6"
if os.name=="nt":
	socket_protocol=socket.IPPROTO_IP
else:
	socket_protocol=socket.IPPROTO_ICMP
sniff=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)
sniff.bind((host,0))

sniff.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

if os.name=='nt':
	sniff.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
print sniff.recvfrom(65565)
if os.name=='nt':
	sniff.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)
	

