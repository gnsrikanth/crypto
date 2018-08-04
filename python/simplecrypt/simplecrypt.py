import sys
from simplecrypt import encrypt,decrypt
import getpass
import os
filename=sys.argv[1]
option=sys.argv[2]
pswd = getpass.getpass('Password:')

def encryptdata():
    f=open(filename,"rb")
    pt=f.read()
    f.close()
    ct=encrypt(pswd,pt)
    f=open(filename,"wb")
    f.write(ct)
    f.close()
    print("[+]Done")
def decryptdata():
    f=open(filename,"rb")
    ct=f.read()
    f.close()
    pt=decrypt(pswd,ct)
    f=open(filename,"wb")
    f.write(pt)
    f.close()
    print("[+]Done")
if os.path.exists(filename) == True:
    if option=="encrypt":
        try:
            encryptdata()
        except:
            print("[-]Cannot encrypt data error"+e)
    elif option=="decrypt":
        try:
            decryptdata()
        except:
            print("[+]Cannot decrypt, Wrong file or password")
    else:
        print("[-]Wrong Options\n[+]Usage: python simplecrypt.py filename encrypt/decrypt")
else:
    print("[-]file not found")
