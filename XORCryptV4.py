#XORCrypt V4
#Using xor to encrypt and decrypt files
#Written by Michael Pavle
import sys
import getopt
from tqdm import *

keyfile = ""
key = bytearray("", "utf-8")
input = ""
output = ""

def usage(argv):
    print("\tXORCrypt - A python tool used for xor encryption")
    print()
    print()
    print("Mandatory:")
    print("\t-k --key - specify XOR key file")
    print("\t-i --input - input file to be encrypted")
    print("\t-o --output - output file for encrypted result (Will overwrite existing data in output file)")
    print()
    print("Optional:")
    print("\t-t --text - write key as text argument")
    print()
    print("Examples:")
    print("\t{} -k keyfile.txt -i secret.png -o enc_secret.png".format(argv[0]))
    print("\t{} --text abc -i passwords.txt -o passwords.txt".format(argv[0]))
    print("\t{} -k summer-2018.png -i photos_07_2018.zip -o photos_07_2018.zip".format(argv[0]))
    print()
    print()
    print("\tNOTE: Decryption key is the same as your encrytion key")
    sys.exit(0)

def main(argv):
    global keyfile
    global key
    global input
    global output

    if not len(argv[1:]):
        usage(argv)
    
    try:
        opts, args = getopt.getopt(argv[1:], "hk:t:i:o:", ["help", "key=", "text=", "input=", "output="])
        
    except getopt.GetoptError as err:
        print(str(err))
        usage(argv)
        
    for o, a in opts:
        if o in ("-h", "--help"):
            usage(argv)
        elif o in ("-k", "--key"):
            keyfile = a
        elif o in ("-t", "--text"):
            key = a.encode("utf-8")
        elif o in ("-i", "--input"):
            input = a
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "Unhandled Option"
    
    if keyfile != "" and key != bytearray("", "utf-8"):
        print("[!] Please enter either a key file or text argument")
        usage(argv)
        
    xor()
def xor():
    print("[*] Program started successfully, no errors\n")
    #variables
    global keyfile
    global key
    global input
    global output
    encrypted = bytearray("", "utf-8")
    
    if keyfile != "":
        f = open(keyfile, "rb")
        #NOTE - key is no longer bytearray, but rather a bytes-like object
        key = f.read()
        key = key.encode("utf-8")
        f.close()
    
    print("[*] Reading data from file...")
    #read data from input file
    f = open(input, "rb")
    content = f.read()
    f.close()
    print("[+] Done!\n")

    #print(content)
    
    print("[*] Beginning file encryption...")
    pbar = tqdm(total = len(content))
    encrypted = bytearray("", "utf-8")
    k = 1
    for byte in content:
        encrypted.append(key[k] ^ byte)
        pbar.update(1)
        k+=1
        #reset key index
        if (k == len(key)):
            k = 0
    content = encrypted
    pbar.close()
    print("[+] Encrypted bytes now saved\n")

    print("[*] Writing encrypted data to output file...")
    f = open(output, "wb")
    f.write(encrypted)
    f.close()
    print("[+] File written successfully! Now exiting...")
    sys.exit(0)
    
if __name__ == "__main__":
    main(sys.argv)
