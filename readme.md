# Python Radius Client/Server mock

Use for inspiration and testing purpose only.

```console
[mock-radius]$ ./server.py
Received an authentication request
Attributes:
User-Name: ['tuser']
User-Password: [b'\x9f\x86@A\xcd\x0b\x84\x92\xb5\x98a{)/\x0f\x01']
Received an authentication request
Attributes:
State: [b'My State']
User-Name: ['tuser']
User-Password: [b'\x08\xa2\xf2\x89\x14\x83\x14l\x8f\x17 {\x1a\xfe?\xaf']


[mock-radius]$ ./client.py
Authenticating...
Challenge: [b'Enter more information']
State: b'My State'
Authentication successful
```
