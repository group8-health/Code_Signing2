from keygen import create_keypair
from product import compose_application_text
from signer import attach_signature
from validator import authenticate_signature

def orchestrate():
    # Generate signing keys if not present
    create_keypair()

    # Simulate original application content
    dev_id = "ID987654321"
    original_content = compose_application_text(dev_id)
    print("\nOriginal App Content:\n", original_content)

    # Sign the application
    attach_signature(original_content)

    # Validate original application
    print("\nAuthenticating Original App:")
    is_authentic = authenticate_signature(original_content)
    print("Verification Result:", is_authentic)

    # Simulate tampered version
    altered_content = original_content + "\nInjected malicious payload!"
    print("\nAuthenticating Tampered App:")
    is_fake = authenticate_signature(altered_content)
    print("Verification Result:", is_fake)

if __name__ == "__main__":
    orchestrate()
