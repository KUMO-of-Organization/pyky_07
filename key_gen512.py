import ccakem
import pickle

priv, pub = ccakem.kem_keygen512()

pubkey = './pubkey512.txt.'
seckey = './seckey512.txt.'

#print(type(pub))
#print(pub)

f_pub = open(pubkey, 'wb')
pickle.dump(pub, f_pub)
print("Generated to pubkey512.txt")

f_sec = open(seckey, 'wb')
pickle.dump(priv, f_sec)
print("Generated to seckey512.txt")

#with open(pubkey, mode="w") as f:
#    f.write(str(pub))

#with open(seckey, mode="w") as f:
#    f.write(str(priv))