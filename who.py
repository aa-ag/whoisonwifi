###--- IMPORTS ---###
from who_is_on_my_wifi import *

info = device()

print(f"PC: {info[0]}")
print(f"PC Product-Name: {info[1]}")
print(f"MAC Address: {info[2]}")
print(f"IP Address (host): {info[3]}")
print(f"IP Address: {info[4]}")
print(f"PC HostName: {info[5]}")
print(f"WiFI Name: {info[6]}")
print(f"Gateway: {info[7]}")
print(f"DNS 1: {info[8]}")
print(f"DNS 2: {info[9]}")
print(f"Password: {info[10]}")
