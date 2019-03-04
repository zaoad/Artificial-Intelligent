def isqrt(n):
    x = n
    y = (x + 1) / 2
    while y < x:
        x = y
        y = (x + n / x) / 2
    return x

def isD(k,d,e,mod):

    if (k==0):
        return False
    if(d%2==0):
        return False
    if(e*d-1)%k!=0:
        return False

    phi = (e*d-1)/k
    a =1
    b = -(mod+1-phi)
    c = mod
    det = b*b - 4*a*c

    detr = isqrt(det)
    #print(detr)
    # check it is an integer root or not.
    if(detr*detr==det):
        return True
    return False

def cf_expansion(n, d):
    e = []

    q = n / d
    r = n % d
    e.append(q)

    while r != 0:
        n, d = d, r
        q = n / d
        r = n % d
        e.append(q)

    return e

def convergents(e,pubKey,mod):
    n = [] # Nominators
    d = [] # Denominators

    for i in range(len(e)):
        if i == 0:
            ni = e[i]
            di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else: # i > 1
            ni = e[i]*n[i-1] + n[i-2]
            di = e[i]*d[i-1] + d[i-2]
       #di is the private key
       #ki is the factor.
        n.append(ni)
        d.append(di)
        if isD(ni,di,pubKey,mod):
            return di
     #   print(ni, di)

def bigmod(x,p,mod):
    if(p==0):
        return 1
    elif(p%2 ==1):
        return (x*bigmod(x,p-1,mod))%mod
    else:
        ret = bigmod(x,p/2,mod)
        return (ret*ret)%mod

def decrypt(ciphertext,pvtKey,mod):
    #because key size is very very large.
    return bigmod(ciphertext,pvtKey,mod)

def main():
    fi = open("4.3_ciphertext.hex","r")
    ciphertext = fi.readline()
    fi.close()

    fi = open("4.4_public_key.hex","r")
    pubkey = fi.readline()
    fi.close()

    fi = open("4.5_modulo.hex","r")
    mod = fi.readline()
    fi.close()

    ciphertext = int(ciphertext,16)
    pubkey = int(pubkey,16)
    mod = int(mod,16)
   # print(ciphertext)
   # print(pubkey)
   # print(mod)

    c = cf_expansion(pubkey, mod)
   # print(c)
    pvtKey = convergents(c,pubkey,mod)
    print("Private Key: "+str(pvtKey))

    plainText = decrypt(ciphertext, pvtKey, mod)
    print("Plain Text: "+str(plainText))


if __name__ == '__main__':
    main()

