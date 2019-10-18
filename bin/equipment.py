from paramiko import SSHClient
import paramiko

class Equipment:
    def __init__(self,ip,port,user,password):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password

    def connect_todevice(self,ip,port,user,password,commandfile):
        try:
            ssh = SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip,username=user,password=password,port=port)
            with open(commandfile) as file_command:
                for line in file_command:
                    stdin,stdout,stderr = ssh.exec_command(line)
                    if stderr.channel.recv_exit_status() != 0:
                        print(stderr.read())
                    else:
                        print(stdout.read())
        except:
            print("Error connecting to {}".format(ip))