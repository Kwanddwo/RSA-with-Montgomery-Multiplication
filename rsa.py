from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util.number import getPrime, GCD

e = 65537

def generate_primes(bits: int):
    while True:
        p = getPrime(bits // 2)
        q = getPrime(bits // 2)
        if p == q:
            continue
        phi = (p - 1) * (q - 1)
        if GCD(e, phi) == 1:
            break
    return p, q

p = 98995185270988407361518907603398703353339360563272113390208346136166438950780849418024395717724037286470262049390402371308011480300643205390672368464183707614243234960393233333994050123990043867926309171573776742062792822553439373652496727336673851585353823378362683516398808996579816371009282125728800340517
q = 94034566061701137726234714742204072353428593008880726932865697679564101150737256107082987763328826610060408696117307395881675795958224729790274294880533445863420919470587044036790719509896970812918048061698861130024932038600495045745891754558132684890031226090998123779466108643209430974433441659046674192919

# p, q = generate_primes(24)

N = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

def exp_modulaire(x, exp, mod):
    curr = x % mod
    if (curr == 0):
        return 0

    res = 1
    while exp:
        if exp & 1:
            res = (res * curr) % mod
        curr = (curr * curr) % mod
        exp >>= 1
    return res

def encrypt(data: bytes):
    m = bytes_to_long(data)
    c = exp_modulaire(m, e, N)
    return long_to_bytes(c)

def decrypt(data: bytes):
    c = bytes_to_long(data)
    m = exp_modulaire(c, d, N)
    return long_to_bytes(m)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("usage: python rsa.py n")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if (n <= 0):
            raise ValueError()
    except e:
        print("usage: python rsa.py n")
        sys.exit(1)

    for i in range(n):
        test = b"this is a very large text that will be used to test out this implementation of the rsa cryptosystem, montgomerry multiplication is an optimization used when multiplying a lot with the same modulus. it is implemented in python's pow"
        print(test)
        print(decrypt(encrypt(test)))
