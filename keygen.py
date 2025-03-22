import os
from ecdsa import SigningKey, SECP256k1

def create_keypair(secret_file='ecdsa_secret.pem', public_file='ecdsa_public.pem'):
    if not os.path.exists(secret_file) or not os.path.exists(public_file):
        signer = SigningKey.generate(curve=SECP256k1)
        verifier = signer.get_verifying_key()

        with open(secret_file, 'wb') as sf:
            sf.write(signer.to_pem())
        with open(public_file, 'wb') as pf:
            pf.write(verifier.to_pem())

        print("New keypair created and stored.")
    else:
        print("Key files already found. Skipping generation.")
