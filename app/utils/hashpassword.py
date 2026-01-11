from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher

# make  an instance with bcrypt hasher
password_hashed = PasswordHash((BcryptHasher(),))


# make  an function to hash the password
def get_password_hash(password):
    return password_hashed.hash(password)


# another function to verify the password
def verify_password(plain_password, hashed_password):
    return password_hashed.verify(plain_password, hashed_password)
