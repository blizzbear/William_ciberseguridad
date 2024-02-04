import random
import hashlib

def generate_primes():
   
    p = 23
    return p

def generate_keys():
   
    a_private = random.getrandbits(256)
    b_private = random.getrandbits(256)

    return a_private, b_private

def compute_public_key(g, private_key, p):
    
    public_key = pow(g, private_key, p)
    return public_key

def compute_secret_key(public_key, private_key, p):
   
    secret_key = pow(public_key, private_key, p)
    return secret_key

def hash_key(key):
    
    hashed_key = hashlib.sha256(str(key).encode()).hexdigest()
    return hashed_key

def main():
    
    p = generate_primes()
    g = 2

   
    a_private, b_private = generate_keys()

   
    A = compute_public_key(g, a_private, p)
    B = compute_public_key(g, b_private, p)

    
    s_alice = compute_secret_key(B, a_private, p)
    s_bob = compute_secret_key(A, b_private, p)

    hashed_s_alice = hash_key(s_alice)
    hashed_s_bob = hash_key(s_bob)

    
    if hashed_s_alice == hashed_s_bob:
        print("Llaves secretas iguales:")
        print("Alice:", hashed_s_alice)
        print("Bob:", hashed_s_bob)
    else:
        print("Error: Las llaves secretas no son iguales.")

if __name__ == "__main__":
    main()
