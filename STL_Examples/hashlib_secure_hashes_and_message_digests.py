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





