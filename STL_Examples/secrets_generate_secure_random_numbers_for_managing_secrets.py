# The secrets module is used for generating cryptographically strong random numbers suitable for
# managing data such as passwords, account authentication, security tokens, and related secrets.
import secrets

print(secrets.token_bytes(16))
print(secrets.token_hex(16))
print(secrets.token_urlsafe(16))