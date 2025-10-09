# import libraries
import os
from cryptography.fernet import Fernet

class RansomWare:

    # The file types this toy will encrypt
    file_exts = ['.txt', '.docx', '.pdf']  # just examples

    def __init__(self, test_folder="ransomware_test_env"):
        
        # This sets up our safe test folder and important variables.
        
        self.localRoot = os.path.join(os.getcwd(), test_folder)
        os.makedirs(self.localRoot, exist_ok=True)  # make folder if not exists

        # Where we'll keep the key file
        self.key_path = os.path.join(self.localRoot, "fernet_key.txt")

        demo_file = os.path.join(self.localRoot, "sample.txt")
        if not os.path.exists(sample_file):
        with open(sample_file, "w") as f:
            f.write("This encryption is for educational purpose")

        # Start with no key or crypter
        self.key = None
        self.crypter = None

    def generate_key(self):
        # Make a new secret key and prepare the encrypt/decrypt tool.
        self.key = Fernet.generate_key()        # make the key
        self.crypter = Fernet(self.key)         # make the tool with that key
        print("✅ Key generated successfully!")

    def write_key(self):
        # Save the secret key safely in our test folder.
        if not self.key:
            print("⚠️ You must generate the key first!")
            return
        with open(self.key_path, "wb") as key_file:
            key_file.write(self.key)
        print(f"🔑 Key saved to: {self.key_path}")

    def load_key(self):
        # Load the key from the text file (so we can use it again).
        if not os.path.exists(self.key_path):
            print("❌ Key file not found! Generate it first.")
            return
        with open(self.key_path, "rb") as key_file:
            self.key = key_file.read()
        self.crypter = Fernet(self.key)
        print("✅ Key loaded successfully!")

    def encrypt_file(self, sample.txt):
        # Encrypt one test file inside the test folder.
        file_path = os.path.join(self.localRoot, sample.txt)
        if not os.path.exists(file_path):
            print("❌ File not found!")
            return

        with open(file_path, "rb") as f:
            data = f.read()

        encrypted = self.crypter.encrypt(data)

        with open(file_path, "wb") as f:
            f.write(encrypted)

        print(f"🔒 {sample.txt} encrypted!")

    def decrypt_file(self, sample.txt):
        # Decrypt one test file inside the test folder.
        file_path = os.path.join(self.localRoot, sample.txt)
        if not os.path.exists(file_path):
            print("❌ File not found!")
            return

        with open(file_path, "rb") as f:
            data = f.read()

        decrypted = self.crypter.decrypt(data)

        with open(file_path, "wb") as f:
            f.write(decrypted)

        print(f"🔓 {sample.txt} decrypted!")
