def encrypt(msg,N):
    c =((msg)**e) %N
    return c

def decrypt(msg,key):
    c = (int(msg)**key)%N
    return c


def egcd(a, b):
	if a==0:
		return (b, 0, 1)
	g, y, x = egcd(b%a, a)
	return (g, x-(b/a) * y, y)

def privateKey(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		print('No modular inverse')
	return x%m

p = input()
q = input()
p = int(p)
q = int(q)
N = p*q
phi  = (p-1)*(q-1)
e = 3
m = input()
rsa_encrypt = encrypt(m,N)
print("encryptedMsg ")
print(rsa_encrypt)
priKey = privateKey(e,phi)
print(priKey)
rsa_decrypt = decrypt(rsa_encrypt,priKey)
print("decryptedMessage")
print(rsa_decrypt)