from os import listdir
from os.path import isfile, join
import os
import sys
from Crypto.Cipher import AES
import hashlib
import base64

def print_usage():
    print('Usage:')
    print('python save_ts.py [encoded binary data] -k [key string] -o [output_filename]')

if len(sys.argv) < 6:
    print_usage()
    sys.exit()

encoded_data_file = sys.argv[1]

key = ''
output_filename = ''

i = 2
while i < len(sys.argv):
    if sys.argv[i] == '-k':
        key = sys.argv[i+1]
        i += 1
        continue
    if sys.argv[i] == '-o':
        output_filename = sys.argv[i+1]
        i += 1
        continue

if key == '' or output_filename == '':
    print('Arguments not enough')
    print_usage()
    sys.exit()

if os.path.exists(output_filename):
    ans = input(f'{output_filename} already exists.\nOverwrite it?[y/n] ==> ')
    if ans != 'y' and ans != 'Y':
        sys.exit()

iv =  b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
key = key.encode('utf-8')

with open(encoded_data_file, 'rb') as fin, open(output_filename, 'wb') as fout:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    fout.write(cipher.decrypt(fin.read()))
