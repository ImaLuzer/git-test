from netmiko import ConnectHandler
from getpass import getpass

device1 = {
   "host": '192.168.20.6',
   "username": 'admin',
   "password": getpass(),
   "device_type": 'cisco_ios',
   "session_log": 'my_session.txt'
   }

net_connect = ConnectHandler(**device1)

print(net_connect.find_prompt())

command = 'show int status'

output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False)

output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)

print(output)

net_connect.disconnect()

