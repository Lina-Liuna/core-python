# This module provides access to the BSD socket interface.

import socket

# Create a new socket using the given address family, socket type and protocol number
# class socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)¶
sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM)

# socket.create_server(address, *, family=AF_INET, backlog=None, reuse_port=False, dualstack_ipv6=False)
# Convenience function which creates a TCP socket bound to address (a 2-tuple (host, port)) and return the socket object.
addr = ("", 8080)  # all interfaces, port 8080
if socket.has_dualstack_ipv6():
    s = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True)
else:
    s = socket.create_server(addr)

# The following example fetches address information for a hypothetical TCP connection to example.org on port 80
print(socket.getaddrinfo("example.org", 80, proto=socket.IPPROTO_TCP))

s1, s2 = socket.socketpair()
b1 = bytearray(b'----')
b2 = bytearray(b'0123456789')
b3 = bytearray(b'--------------')
print(s1.send(b'Mary had a little lamb'))
s2.recvmsg_into([b1, memoryview(b2)[2:9], b3])
print([b1, b2, b3])
