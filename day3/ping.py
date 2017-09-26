'''
ping a list of hosts to check status
'''

import os


def clean_hosts(x):
    x = x.strip()
    print x
    if not x.startswith('#'):
        return x
    return None


fin = open("hosts.txt", "r")
# hosts = map(lambda x: x.rstrip() if not x.lstrip().startswith('#') else pass , fin.readlines())
# hosts = filter(lambda x: x.strip() if not x.lstrip().startswith('#') else None, fin.readlines())
hosts = filter(clean_hosts, fin.readlines())
fin.close()
print hosts


def isdown(host, n=1):
    pingstr = "ping {} -n {} >> ping.log"
    return os.system(pingstr.format(host, n))


for host in hosts:
    if isdown(host):
        print host + " is down"
    else:
        print host + " is up"
