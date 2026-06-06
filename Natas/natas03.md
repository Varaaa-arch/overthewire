# Natas Level 3

### Level Goal
> The goal of this level is to find the password for the next level.

### Discovery & Logic
1. **Analysis**: The page says "There is nothing on this page". Viewing the source reveals a hint: `<!-- No more information leaks!! Not even Google will find it this time... -->`.
2. **Problem**: The hint mentions Google — this is a reference to `robots.txt`, a file used to tell search engine crawlers which directories to avoid indexing.
3. **Solution**: Navigate to `/robots.txt` to find hidden directories, then browse to the disallowed path to find `users.txt` containing the password.

### Commands Used
```
URL   : http://natas3.natas.labs.overthewire.org
User  : natas3
```

Check `robots.txt`:
```
http://natas3.natas.labs.overthewire.org/robots.txt
```

content of `robots.txt`:
```
User-agent: *
Disallow: /s3cr3t/
```

Navigate to the disallowed directory:
```
http://natas3.natas.labs.overthewire.org/s3cr3t/
```

Open `users.txt`:
```
http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
```

Content of `users.txt`:
```
natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ
```

### What I Learned
* **robots.txt is Not a Security Measure**: `robots.txt` is a convention for search engine crawlers, not an access control mechanism. Anyone can read it and find the "hidden" paths.
* **Security Through Obscurity Fails**: Hiding a directory with an obscure name and listing it in `robots.txt` is counterproductive — it actively advertises the secret path to attackers.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ</code>
</details>
