import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256 as hash
class rsa:
	def rsakeys():
		length=1024
		privatekey = RSA.generate(length, Random.new().read)
		publickey = privatekey.publickey()
		return privatekey, publickey
	def exportkeys(publickey,privatekey,private_file,public_file):
		f=open(private_file,"w")
		f.write((privatekey.exportKey('PEM')).decode())
		f.close()
		f=open(public_file,"w")
		f.write((publickey.exportKey('PEM')).decode())
		f.close()
privatekey,publickey=rsa.rsakeys()
exportkeys(privatekey,publickey,"private.key","public.key")
print("[+]privatekey.key,publickey.key has been generated")
