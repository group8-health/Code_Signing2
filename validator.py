import hashlib
from ecdsa import VerifyingKey, BadSignatureError

def authenticate_signature(app_content, signature_path='signed_output.sig', pub_key_path='ecdsa_public.pem'):
    with open(pub_key_path, "rb") as pk_file:
        verifier = VerifyingKey.from_pem(pk_file.read())

    digest = hashlib.sha256(app_content.encode('utf-8')).digest()

    with open(signature_path, "rb") as sig_file:
        retrieved_sig = sig_file.read()

    try:
        if verifier.verify(retrieved_sig, digest):
            print("Validation successful: trusted source confirmed.")
            return True
        else:
            print("Validation failed: integrity compromised.")
            return False
    except BadSignatureError:
        print("Invalid signature: tampering detected.")
        return False
