###--- IMPORTS ---###
import scapy.all as scapy


###--- NETWORK SCANNER ---###
request = scapy.ARP()

print(request.summary())
print(request.show())
