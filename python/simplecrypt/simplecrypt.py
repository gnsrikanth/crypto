import sys
from simplecrypt import encrypt,decrypt
import getpass
filename=sys.argv[1]
option=sys.argv[2]
pswd = getpass.getpass('Password:')
if option=="encrypt":
    f=open(filename,"rb")
    data=f.read()
    f.close()
    ct=encrypt(data,pswd)
    f=open(filename,"wb")
    f.write(ct)
    f.close()
elif option=="decrypt":
    f=open(filename,"rb")
    ct=f.read()
    f.close()
    pt=decrypt(ct,paswd)
    f=open(filename,"wb")
    f.write(pt)
    f.close()
