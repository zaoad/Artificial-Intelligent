from Crypto.PublicKey import RSA

def main():
    key = open("rsa_key","r").read()
    keypub = open("rsa_key.pub","r").read()
    rsaPri = RSA.importKey(key)
    rsaPub = RSA.importKey(keypub)

    message = "hello world"
    print(message)

    c = rsaPub.encrypt(message,"")
    print("Encrypted Message: " +str(c))
    p = rsaPri.decrypt(c)
    print("Decrypted Message: "+str(p))

if __name__ == "__main__":
    main()