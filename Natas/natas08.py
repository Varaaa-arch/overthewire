import binascii, base64

encoded = "3d3d516343746d4d6d6c315669563362"
secret = base64.b64decode(binascii.unhexlify(encoded)[::-1]).decode()
print(f"{secret}") 
