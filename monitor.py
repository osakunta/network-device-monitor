from sample.ping import ping
from data.data import hosts

for host in hosts:
    ping(host)
