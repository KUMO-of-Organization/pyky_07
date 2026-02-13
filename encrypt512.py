import ccakem
import os
import pickle
from getpass import getpass

seed = input("種をを32byteで入力してください。:")
#seed = str(getpass("種をを32byteで入力してください。:"))
seed = seed.encode('utf-8')
print("seed=" + str(seed))

f = open("./pubkey512.txt","rb")
pub_key = pickle.load(f)

#print(pub_key)
#print(type(pub_key))

secret1, cipher = ccakem.kem_encaps512(pub_key,seed)

print(cipher)
print(secret1)

f_cip = open("./cipher512.txt", 'wb')
pickle.dump(cipher, f_cip)
print("Generated to cipher512.txt")

with open("./shared_secret512.txt", mode="w") as f:
    f.write(str(secret1))
print("Generated to shared_secret512.txt")
