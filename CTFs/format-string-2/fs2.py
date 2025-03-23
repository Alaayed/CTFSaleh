from pwn import *

binary = ELF('bin-format-string-2')
sus_location = binary.symbols['sus']
print('Hey')
print(sus_location)
hex_location = hex(sus_location)
print(hex_location)


# stack print from challenge
stack = " 0x402075|(nil)|0x71d7525cea00|(nil)|0x16f852b0|0x71d752620af0|0x71d7525f74e8|0x71d7525f7de9|0x71d7523c8098|0x71d7525e44d0|(nil)|0x7ffe76b71520|0x3036303430347830"
addresses = stack.split(sep='|')
print(addresses)
# Hm, closest address seams to be the first, lets find the distance between them
delta = 0x402075-0x404060
hex_location =0x404060
for i, address in enumerate(addresses):
    if address.startswith('0x'):
        byte_value = bytes.fromhex(address[2:])
        string_rep = byte_value[::-1].decode()
        print(string_rep)