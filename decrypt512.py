import ccakem
import pickle

f_sec = open("./seckey512.txt","rb")
sec_key = pickle.load(f_sec)

f_cip = open("./cipher512.txt","rb")
cipher = pickle.load(f_cip)

secret2 = ccakem.kem_decaps512(sec_key, cipher)
print(secret2)