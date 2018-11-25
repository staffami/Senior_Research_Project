import requests
import paramiko
from random import randint, choice

# Static list of traffic types
traffic_types = ['http', 'dns', 'dhcp', 'icmp', 'ssh', 'ftp']

###############################################################
# traffic_bool: Returns boolean based on randint

def traffic_bool():
    # Generate random number between 0 and 2000
    rand = randint(0, 2000)

    # Modulus random number by 2 to determine boolean
    if rand % 2 == 0:
        return True
    else:
        return False

###############################################################
# determine_traffic: Returns traffic type based on random number

def determine_traffic():
    return choice(traffic_types)

###############################################################
# http(s) handler

def http_handler():
    pass

###############################################################
# dns handler

def dns_handler():
    pass

###############################################################
# dhcp handler

def dhcp_handler():
    pass

###############################################################
# icmp handler

def icmp_handler():
    pass

###############################################################
# ssh handler

def ssh_handler():
    pass

###############################################################
# ftp handler

def ftp_handler():
    pass

###############################################################
# Main

def main():
    print(traffic_bool())
    print(traffic_types)
    print(determine_traffic())


###############################################################
# Initiator

if __name__ == "__main__":
    main()