#! /usr/bin/python3
# secures user password to store it in database
# uses sha512

# import modules
import getpass
import hashlib
import uuid

# secure the password
def hashpwd(f_password):
    uuid_2ba = uuid.uuid4().hex     # generate a random hex UUID
    
    p_pwd = hashlib.sha512(uuid_2ba.encode() + f_password.encode()).hexdigest() + ':' + uuid_2ba
    return p_pwd


# check successive inputs
def checkpwd(hashed_password, c_password):
    genF_part, uuid_2ba = hashed_password.split(':')

    return genF_part == hashlib.sha512(uuid_2ba.encode() + c_password.encode()).hexdigest()


while True:
    f_password = getpass.getpass(prompt='Please enter your password: ')
    hashed_pwd = hashpwd(f_password)

    crnt_pwd = getpass.getpass(prompt='Enter the password again: ')

    if checkpwd(hashed_pwd, crnt_pwd):
        print('Successful entry, congratulations!\n')
        break
    else:
        print("Passwords don't match. Try again...")   
    