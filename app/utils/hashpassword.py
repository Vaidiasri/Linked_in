from pwdlib import PasswordHash
# make  an instance 
password_hashed= PasswordHash.recommended()
# make  an function to hash the password
def get_password_hash(password):
    return password_hashed.hash(password)
# another function to verify the password 
def verify_password(plain_password, hashed_password):
    return password_hashed.verify(plain_password, hashed_password)