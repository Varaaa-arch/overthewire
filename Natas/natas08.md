# Natas Level 8

> 🎥 **Video Walkthrough**: [Watch on YouTube](https://youtu.be/Gq-sP7r4c24?si=H2a9DXf76BTqNl8h)

### Discovery & Logic
1. **Analysis**: The page shows a form asking for a **secret**, with a link to view the source code.
2. **Problem**: The source code reveals how the secret is encoded before comparison:
   ```php
   $encodedSecret = "3d3d516343746d4d6d6c315669563362";

   function encodeSecret($secret) {
       return bin2hex(strrev(base64_encode($secret)));
   }
   ```
3. **Solution**: Reverse the encoding steps to recover the original secret.

### Reversing the Encoding

Encoding order: `base64_encode` → `strrev` → `bin2hex`

Reverse order: `hex2bin` → `strrev` → `base64_decode`

### Source Code
[natas08.py](natas08.py)

### Commands Used

```python
import binascii, base64

encoded = "3d3d516343746d4d6d6c315669563362"
secret = base64.b64decode(binascii.unhexlify(encoded)[::-1]).decode()
print(f"{secret}")
```

### What I Learned
* **Reverse Engineering Encoding**: Encoding is not encryption. Any encoding scheme (base64, hex, etc.) can be reversed if you know the algorithm.
* **Source Code Disclosure**: Exposing the encoding logic in source code allows attackers to fully reverse-engineer the expected input.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t</code>
</details>
