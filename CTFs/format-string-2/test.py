test_string = "0x3036303430347830"
test_string = test_string[2:]
byte_data = bytes.fromhex(test_string)
reverse_data = byte_data[::-1]
string_rep = reverse_data.decode()
print(string_rep)
print(byte_data.decode())

test_string = test_string[::-1]
byte_data = bytes.fromhex(test_string)
string_rep = byte_data.decode()
print(string_rep)