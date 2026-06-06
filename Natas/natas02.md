# Natas Level 2

### Level Goal
> The goal of this level is to find the password for the next level.

### Discovery & Logic
1. **Analysis**: The page says "There is nothing on this page", but inspecting the source reveals an `<img>` tag pointing to `files/pixel.png`.
2. **Problem**: The password is not in the HTML source directly, but the `files/` directory might contain other files.
3. **Solution**: Navigate to `http://natas2.natas.labs.overthewire.org/files/` the server has **directory listing** enabled, revealing a file called `users.txt` which contains the password.

### Commands Used
```
URL   : http://natas2.natas.labs.overthewire.org
User  : natas2
```

Navigate to the exposed directory:
```
http://natas2.natas.labs.overthewire.org/files/
```

Open `users.txt`:
```
http://natas2.natas.labs.overthewire.org/files/users.txt
```

Content of `users.txt`:
```
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
eve:zo4mJWyNj2
mallory:9urtcpzBmH
```

### What I Learned
* **Directory Listing**: When a web server has directory listing enabled, anyone can browse the contents of a folder like a file explorer — sensitive files should never be in publicly accessible directories.
* **Exposed Sensitive Files**: Files like `users.txt` containing credentials should never be placed in a web-accessible path.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH</code>
</details>
