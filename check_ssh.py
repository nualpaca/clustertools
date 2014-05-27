import paramiko, colorama, select, socket
colorama.init(autoreset=True)

from colorama import Fore
from paramiko import AuthenticationException, SSHException, BadHostKeyException

servers = open('servers.txt').read().splitlines()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

test_python = True
counter = 0

print ""

for server in servers:
    try:
        ssh.connect(server, username='asj936', timeout=0.5)

        if test_python == True:
            (stdin1, stdout1, stderr1) = ssh.exec_command('which python')
            python_location = stdout1.read().strip()

            # python --version wasn't working for god knows what reason
            (stdin2, stdout2, stderr2) = ssh.exec_command('python -c "import sys; print sys.version[:6]"')
            python_version = stdout2.read().strip()

            (stdin3, stdout3, stderr3) = ssh.exec_command('which pip')
            pip_location = stdout3.read().strip()

            (stdin4, stdout4, stderr4) = ssh.exec_command('pip --version')
            pip_version = stdout4.read().strip()[3:9]
        else:
            python_location = ""
            python_version = ""
            pip_location = ""
            pip_version = ""

        ssh.close()
    except (AuthenticationException, SSHException, BadHostKeyException, socket.error) as e:
        print server.ljust(45) + Fore.RED + str(e).ljust(20)
        continue

    counter += 1
    print server.ljust(45) + Fore.GREEN + "okay".ljust(10) + Fore.RESET + python_location.ljust(30) + python_version.ljust(15) + pip_location.ljust(25) + pip_version

print "======================================================"
print "Active Servers: " + str(counter)
print "Total Servers: " + str(len(servers))