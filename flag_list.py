def str_from_str(filename):
    with open(filename) as f:
        for line in f:
            string = line
            print(string,end='')
    print()

def str_from_hex(filename):
    with open(filename) as f:
        for line in f:
            string = hex(int((line.encode('UTF-8')).hex(), base=16))[2:]
            print(string)

def str_from_int(filename):
    with open(filename) as f:
        for line in f:
            string = int((line.encode('UTF-8')).hex(), base=16)
            print(string)

def str_from_bin(filename):
    with open(filename) as f:
        for line in f:
            string = bin(int((line.encode('UTF-8')).hex(), base=16))[2:]
            print(string)

def str_from_oct(filename):
    with open(filename) as f:
        for line in f:
            string = oct(int((line.encode('UTF-8')).hex(), base=16))[2:]
            print(string)

def str_from_base64(filename):
    with open(filename) as f:
        for line in f:
            string = base64.b64encode(line.encode())
            print(string)

def str_from_base32(filename):
    with open(filename) as f:
        for line in f:
            string = base64.b32encode(line.encode())
            print(string)

def str_from_byte(filename):
    with open(filename) as f:
        for line in f:
            string = bytes(line, 'ascii')[:-1]
            print(string)

def str_from_ascii(filename):
    with open(filename) as f:
        for line in f:
            for symbol_1 in line:
                print(ord(symbol_1),end = '')
            print()
            for symbol_2 in line:
                print(ord(symbol_2),end = ' ')
            print()

str_from_str('Example_flags')
str_from_hex('Example_flags')
str_from_int('Example_flags')
str_from_bin('Example_flags')
str_from_oct('Example_flags')
str_from_base64('Example_flags')
str_from_base32('Example_flags')
str_from_byte('Example_flags')
str_from_ascii('Example_flags')



