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

def generate_10_alphanumberic_lowercase_upercase_digit_inside():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >=3):
            break
    return password

print(generate_10_alphanumberic_lowercase_upercase_digit_inside())

def generate_url_safe():
    url = 'https://example.com/reset=' + secrets.token_urlsafe()
    return url
print(generate_url_safe())