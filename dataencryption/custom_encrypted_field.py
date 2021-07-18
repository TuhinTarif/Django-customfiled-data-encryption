from django.db.models import TextField
from django.db.models import CharField
from cryptography.fernet import Fernet
import os
from encryptionfield.settings import BASE_DIR

# Generating the key and writing it to a file
"""
to genarate key, Open python shell from pipenv/virtual environment and run following command:
from dataencryption.custom_encrypted_field import genwrite_key
then key will be generate and save it into a new file called pass.key

"""
def genwrite_key():
    key = Fernet.generate_key()
    # with open(os.path.join(BASE_DIR,'dataencryption/pass.key'), "wb") as key_file:
    with open(os.path.join(BASE_DIR,'dataencryption/pass.key'), "wb") as key_file:
        key_file.write(key)

# Function to load the key
def call_key():
    return open(os.path.join(BASE_DIR,'dataencryption/pass.key'), "rb").read()

def encrypt(value):
    if value is None or value == '':
        return value
    encoded_value = value.encode()
    encrypted_value = Fernet(call_key()).encrypt(encoded_value)
    return encrypted_value.decode()

def decrypt(value):
    if value is None or value == '':
        return value
    try: 
        encoded_value = value.encode()  
        decrypted_value = Fernet(call_key()).decrypt(encoded_value)
        return str(decrypted_value.decode())
    except:
        print('error')


class EncryptedTextField(TextField):

    def from_db_value(self, value, expression, connection): 
        return decrypt(value)

    def to_python(self, value):
        return decrypt(value)
            
    
    def get_prep_value(self, value):
        return encrypt(value)


class EncryptedCharField(CharField):
    def from_db_value(self, value, expression, connection): 
        return decrypt(value)

    def to_python(self, value):
        return decrypt(value)
            
    
    def get_prep_value(self, value):
        return encrypt(value)

