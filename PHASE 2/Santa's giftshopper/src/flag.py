from pwn import *


host = 'portal.hackazon.org'
port = 17005

r = remote(host, port)

for i in range(1000):
    r.send("n\n")

# Receive response
print(r.recv())
r.interactive()