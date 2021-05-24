#!/usr/bin/python3

import radius

r = radius.Radius("Secret123", host='localhost')

try:
    print("Authenticating...")
    result = r.authenticate("tuser", "Secret123")
except radius.ChallengeResponse as e:
    print(f"Challenge: {e.messages}")
    print(f"State: {e.state}")

    attrs = {'State': e.state} if e.state else {}
    result = r.authenticate("tuser", "Response", attributes=attrs)

if result:
    print("Authentication successful")
else:
    print("Authentication failure")
