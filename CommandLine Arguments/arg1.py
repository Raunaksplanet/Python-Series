#!/usr/bin/python3

import sys
import base64

cypherList = ["-b64e","-b64d","-b32e","-b32d"]

if "-h" in sys.argv or "--help" in sys.argv or len(sys.argv)==1:
	print(f'''Simple tool to Decode and Encode base64 and base32 data
{sys.argv[0]} -h    | --help [for Help]
	  -b64e [Cipher] To Encode base64
          -b64d [Cipher] To Decode base64
	  -b32e [Cipher] To Encode base32
          -b32d [Cipher] To Decode base32''')
	sys.exit()

for i in range(1, len(sys.argv)):
    if sys.argv[i].startswith("-"):
        if sys.argv[i] == "-b64e" and i + 1 < len(sys.argv):
            encoded_string = sys.argv[i + 1].encode()
            print("Base64 Encoded Data: ", base64.b64encode(encoded_string).decode())
            sys.exit()

        elif sys.argv[i] == "-b64d" and i + 1 < len(sys.argv):
            encoded_string = sys.argv[i + 1].encode()
            print("Base64 Decoded Data: ", base64.b64decode(encoded_string).decode())
            sys.exit()

        elif sys.argv[i] == "-b32e" and i + 1 < len(sys.argv):
            encoded_string = sys.argv[i + 1].encode()
            print("Base32 Encoded Data: ", base64.b32encode(encoded_string).decode())
            sys.exit()

        elif sys.argv[i] == "-b32d" and i + 1 < len(sys.argv):
            encoded_string = sys.argv[i + 1].encode()
            print("Base32 Decoded Data: ", base64.b32decode(encoded_string).decode())
            sys.exit()
else:
	sys.stderr.write("Wrong input, check -h for help")
	sys.exit()


if len(sys.argv) == 2:
	print(f"{sys.argv[1]} cypher Required")
	sys.exit()


if ("-b64e" not in sys.argv or "-b64d" not in sys.argv 
 or "-b32e" not in sys.argv or "-b32d" not in sys.argv): 
	sys.stderr.write("Encoding is not supported")
