# hashlib module implements a common interface to many different secure hash and message digest algorithms.

# included FIPS secure hash algorithms SHA1, SHA224, SHA256, SHA384 and SHA512 as well as RSA's MD5 algorithm.
import hashlib

def get_hash_str_digest(str):
    m = hashlib.sha256()
    m.update(str)
    return m.digest()

def get_hash_str_hex_digest(str):
    m = hashlib.sha256()
    m.update(str)
    return m.hexdigest()

def get_hash_str_digest_desired_algo(algo, str):
    h = hashlib.new(algo)
    h.update(str)
    return h.hexdigest()

str = b"Fortunate Perhaps Infantile"
print(get_hash_str_hex_digest(str))
print(get_hash_str_digest(str))
print(hashlib.sha256(str).digest())
print(get_hash_str_digest_desired_algo('sha1', str))
print(get_hash_str_digest_desired_algo('sha224', str))
print(get_hash_str_digest_desired_algo('sha256', str))
print(get_hash_str_digest_desired_algo('md5', str))


# key derivation
# key derivation and key stretching algorithms are designed for secure password hashing.
# navie algorithms such as SHA1 are not resistant against brute-force attacks.
# A good password hashing function must be tunable, slow, and include a salt.

from hashlib import pbkdf2_hmac


def hash_password_robust(hash_algo,password_str, salt_str):
    our_app_iters = 500_000
    dk = pbkdf2_hmac(hash_algo, password_str, salt_str * 2, our_app_iters)
    return dk.hex()

print(hash_password_robust('sha256', b'linaliu_password', b'bad salt'))
print(hash_password_robust('sha256', b'linaliu_password', b'good salt'))

# BLAKE2
# BLAKE2 is  a cryptographic hash function defined in RFC 7693 that comes in two flavors
# BLAKE2 support keyed mode(a faster and simpler replacement for HMAC), salted hashing,
# personalization, and tree hashing


def simple_hashing_str_using_blake2b(hash_str):
    return hashlib.blake2b(hash_str).hexdigest()


def simple_hashing_str_list_blake2b(hash_str_list):
    h = hashlib.blake2b()
    for item in hash_str_list:
        h.update(item)
    return h.hexdigest()


def key_hashing_str_using_blak22b(hash_str, key_str):
    h = hashlib.blake2b(key=key_str, digest_size=20)
    h.update(hash_str)
    return h.hexdigest()

print(simple_hashing_str_using_blake2b(b'hash me'))
print(simple_hashing_str_list_blake2b([b'hash', b' ', b'me']))
print(key_hashing_str_using_blak22b(b'hash me', b'hard key'))













