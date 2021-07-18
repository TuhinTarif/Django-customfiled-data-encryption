from django.db import models
from dataencryption.custom_encrypted_field import EncryptedTextField, EncryptedCharField

# Create your models here.

class UserProfile(models.Model):

    bank_name = EncryptedCharField(max_length = 255, null = True, blank = True)
    bank_account = EncryptedTextField()

    def __str__(self):
        return self.bank_name
