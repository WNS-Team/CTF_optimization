from pwn import *

int.from_bytes(b'\x00\x01', "big")
int.from_bytes(b'\x00\x01', "little")


# Generate alpabet

def alph_generate():
    alph = []
    for char in string.printable:
        alph.append(hex(ord(char))[2:])
    return (alph)


# Decode hex from string

def hex_from_str(filename):
    with open(filename) as f:
        hex_str = (f.read())
    return bytearray.fromhex(hex_str).decode()


# Decode int from hex

def int_from_hex(filename):
    with open(filename) as f:
        str_int = (f.read())
    return hex(str_int)


# Decode string from int  UTF-8

def str_from_int_UTF8(filename):
    with open(filename, 'rb') as f:
        string = (f.read())
    return int((string.encode('UTF-8')).hex(), base=16)


# Decode string from hex

def str_from_hex(filename):
    with open(filename) as f:
        string = (f.read())
    return hex(int((string.encode('UTF-8')).hex(), base=16))[2:]


# Decode hex from byte

def hex_from_byte(filename):
    with open(filename) as f:
        msg = binascii.unhexlify(f.read())
    return msg


# This is fuction in task

def encrypt(char):
    return (123 * char + 18) % 256


# by msg.enc

def XOR_decrypt_BabyEncryption(filename):
    og_msg = []
    msg = hex_from_byte(filename)
    for byte in msg:
        for i in range(1, 129):
            encrypted = encrypt(i)  # This is function in XOR_code(Task)
            if encrypted == byte:
                og_msg.append(chr(i))
    return ''.join(og_msg)


# by flags.txt

def XOR_Brute_hex(filename):
    with open(filename) as f:
        for line in f.readlines():
            for byte in range(256):
                dec = xor(byte, bytes.fromhex(line))
                if b'dam' in dec:
                    return (dec)
                # print(dec)


"""if b'dam' in dec:  # dam is key-word this flag or all whis commenst - if b'd' in dec:        clear                                
           if b'd' in dec:
           	return(dec)
"""


# by XOR.enc

def XOR_Brute_str(filename):
    cipher = hex_from_str(filename)
    for i in range(256):
        result = ''
        for j in cipher:
            result += chr(i ^ (ord(j)))
            # if 'inter' in result:  # inter is key-word this flag or all whis commenst - #if b'd' in dec:
        print(result)


# by hexstrings(MD5)

def MD5_hex_decrypt(filename):
    a = open(filename).read().splitlines()
    md5s = {}
    for i in range(256):
        md5s[hashlib.md5(chr(i).encode()).hexdigest()] = chr(i)
    flag = ""
    for line in a:
        flag += md5s[line]
    return flag


# by folder challnge RSA

def RSA(filename, d, n):
    for i in range(49):
        with open(filename + str(i) + '.txt', 'rb') as file:
            text = file.read()
            plain = str(hex(pow(int.from_bytes(text, "big"), d, n)))[2::]
            print(''.join([chr(int(''.join(c), 16)) for c in zip(plain[0::2], plain[1::2])]))
        # print(int.from_bytes(text,"big"))


# by Messi.txt

def XOR_whith_part_plaitext(filename):
    part_of_msg = 'Plaintext'
    with open(filename) as f:
        msg = (f.read())
    for i in range(len(msg)):
        candidate = xor(msg[i:i + len(part_of_msg)], part_of_msg)
        if candidate.isalnum():
            print(candidate)


# print(XOR_Brute_hex('flags.txt'))

# print(str_from_int_UTF8('/home/kali/Desktop/CTFd/RootMe/ch30/message1'))

print(str_from_hex('flag.enc'))
