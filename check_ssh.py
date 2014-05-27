import paramiko, colorama
colorama.init(autoreset=True)

servers = open('servers.txt').read().splitlines()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

counter = 0

print ""

for server in servers:
    try:
        ssh.connect(server, username='asj936', timeout=0.5)
    except Exception as e:
        print server.ljust(45) + colorama.Fore.RED + str(e)
        continue
    counter += 1
    print server.ljust(45) + colorama.Fore.GREEN + "okay"

print "======================================================"
print "Active Servers: " + str(counter)
print "Total Servers: " + str(len(servers))