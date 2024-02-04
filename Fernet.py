from cryptography.fernet import Fernet
#encriptacion de mi mensaje 
clave = Fernet.generate_key()
f= Fernet(clave)
print(clave)
token= f.encrypt(b"robi te amo")
print(token)
des = f.decrypt(token)
print(des)

#desencriptacion del mensaje de mi compañero
g = Fernet(b'BB3fgtDnfC-KxNW6pVxyjtBtxgcMTWqDHfc5M3vOIZc=')
mens=g.decrypt(b'gAAAAABluw5TP8E0ogCpLKFsRfZHhU4A5iytfiO83w_GyyMuV4HbnDwvwy4z25zKU2GFI042oesy8B3PV7IeAwGa2wD5Wlb8R1C5bHjxTpd4mNCMSuJ1m7Q=')
print(mens)


