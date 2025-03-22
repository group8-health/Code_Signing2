import hashlib
from ecdsa import SigningKey

def attach_signature(app_content, secret_key='ecdsa_secret.pem', output_sig='signed_output.sig'):
    with open(secret_key, "rb") as key_file:
        signer = SigningKey.from_pem(key_file.read())

    content_digest = hashlib.sha256(app_content.encode('utf-8')).digest()
    encoded_sig = signer.sign(content_digest)

    with open(output_sig, "wb") as sig_file:
        sig_file.write(encoded_sig)

    print("Digital signature attached.")
    print("Signature (hex format):", encoded_sig.hex())
