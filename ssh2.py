import socket,paramiko,threading,sys
#host_key=paramiko.RSAKey(filename='rsakey.py')
uname=raw_input("Enter the username:")
pwd=raw_input("Enter the password:")
class Server(paramiko.ServerInterface):
	def _init_(self):
		self.event=threading.Event()
	def check_channel_request(self,kind,chanid):
		if kind=='session':
			return paramiko.OPEN_SUCCEEDED
		return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
	def check_auth_password(self,username,password):
		if(username==uname)and(password==pwd):
			return paramiko.AUTH_SUCCESSFUL
		return paramiko.AUTH_FAILED
server=sys.argv[1]
ssh_port=int(sys.argv[2])
try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((server, ssh_port))
	sock.listen(100)
	print '[+] Listening for connection ...'
	client, addr = sock.accept()
except Exception, e:
	print '[-] Listen failed: ' + str(e)
	sys.exit(1)
print '[+] Got a connection!'
try:
	bhs=paramiko.Transport(client)
	bhs=add_server_key(host_key)
	server=Server()
	try:
		bhs.start_server(server=server)
	except paramiko.SSHException,x:
		print "[-] SSH Negotiation failed"
	chan=bhs.accept(20)
	print "[+] Authenticated!"
	print chan.recv(1024)
	chan.send("SSH connection is established!")
	while True:
		try:
			command=raw_input("Enter command: ").strip('\n')
			if command!= 'exit':
					chan.send(command)
					print chan.recv(1024)+'\n'
			else:
				chan.send('exit')
				print 'exiting..'
				bhs.close()
				raise Exception('exit')
		except KeyboardInterrupt:
			bhs.close()
		
except Exception,e:
	print '[-] Caught exception: '+str(e)
	try:
		bhs.close()
	except:
		pass
	sys.exit(1)
	
