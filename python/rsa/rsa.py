import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5

class ersa:
	def rsakeys():
		length=1024
		privatekey = RSA.generate(length, Random.new().read)
		publickey = privatekey.publickey()
		return privatekey, publickey
