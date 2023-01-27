# The secrets module is used for generating cryptographically strong random numbers suitable for
# managing data such as passwords, account authentication, security tokens, and related secrets.
import secrets
import string

print(secrets.token_bytes(16))
print(secrets.token_hex(16))
print(secrets.token_urlsafe(16))

def generate_8_alpha_numeric_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(8))
    return password

print(generate_8_alpha_numeric_password())

