# XORCrypt-Python
XOR encryption program I built in python a couple years ago.

Usage:
        XORCrypt - A python tool used for xor encryption


Mandatory:
        -k --key - specify XOR key file
        -i --input - input file to be encrypted
        -o --output - output file for encrypted result (Will overwrite existing data in output file)

Optional:
        -t --text - write key as text argument

Examples:
        XORCryptV4.py -k keyfile.txt -i secret.png -o enc_secret.png
        XORCryptV4.py --text abc -i passwords.txt -o passwords.txt
        XORCryptV4.py -k summer-2018.png -i photos_07_2018.zip -o photos_07_2018.zip


        NOTE: Decryption key is the same as your encrytion key
        
This program works in 3 steps. First, it reads the content of the key file (if provided) and input file. Once all the content is parsed in a bytearray object, the program will loop through each byte in the input file and key, XOR-ing them and appending them to an "encrypted" bytearray. The data is then written to the output file at the end of the program.

It's important to note that since this program is not optimized for large files due to memory issues (loading all content at once), it may crash unless you keep the files small.
