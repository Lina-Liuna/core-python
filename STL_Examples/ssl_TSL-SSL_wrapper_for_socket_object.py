# ssl module provides access to Transport Layer Security(often known as "secure sockets layer") encryption
# and peer authentication facilities for network sockets, both client-side and server-side.

# This module uses the OpenSSL library.

import socket
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

hostname = 'www.python.org'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
