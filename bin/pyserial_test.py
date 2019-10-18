import equipment
import argparse

parser = argparse.ArgumentParser()
group = parser.add_argument_group('group')
group.add_argument('host',help='Mandatory: Define the host, can be the hostname, FQDN or IP address')
group.add_argument('port',help='Define the port to connect via SSH. Default port: 22')
group.add_argument('user',help='Mandatory: The user that will connect to the host.')
group.add_argument('password',help='Mandatory: Password for the user')
group.add_argument('commandfile',help='Mandatory: File with the commands')
args = parser.parse_args()