import sys

def print_usage():
    print('python encode.py -i [input_file] -k [key] (-o [output_file])(optional)')
    print('[key] should not contain space and space-like character')

argc = len(sys.argv) 
if argc != 5 and argc != 7:
    print_usage()
    sys.exit()

input_file = None
output_file = None
key = None
i = 1
while i < argc:
    if sys.argv[i] == '-i':
        input_file = sys.argv[i+1]
        i += 2
        continue
    if sys.argv[i] == '-k':
        key = sys.argv[i+1].strip().strip('\r\n').encode('utf-8')
        i += 2
        continue
    if sys.argv[i] == '-o':
        output_file = sys.argv[i+1]
        i += 2

if input_file == None:
    print('No input file specified!')
    print_usage()
    sys.exit()

if key == None:
    print('No key specified!')
    print_usage()
    sys.exit()

key_len = len(key)

if output_file == None:
    output_file = input_file + '.encode'

chunk_size = key_len

with open(input_file, "rb") as fin, open(output_file, "wb") as fout:
    while True:
        chunk = fin.read(chunk_size)
            
        if chunk == b'':
            break # end of file

        barray = bytearray(chunk)

        for i in range(len(barray)):
            barray[i] = (barray[i] + key[i]) % 256
            
        fout.write(barray)
