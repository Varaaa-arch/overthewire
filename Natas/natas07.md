# Natas Level 7

> 🎥 **Video Walkthrough**: [Watch on YouTube](https://youtu.be/Hmir8QZZJLw?si=NplbVpbf_1DjuyeR)

### Level Goal
> The goal of this level is to find the password for the next level.

### Discovery & Logic
1. **Analysis**: The page has two links — **Home** and **About** — which load pages via a `page` parameter: `?page=home` and `?page=about`.
2. **Problem**: The source code hint says the password is at `/etc/natas_webpass/natas8`. The `page` parameter is passed directly to a PHP `include()` — a classic **Local File Inclusion (LFI)** vulnerability.
3. **Solution**: Replace the `page` value with the absolute path to the password file.

### Steps with Burp Suite

1. Open Burp Suite, **Intercept is ON**.
2. Navigate to `http://natas7.natas.labs.overthewire.org/` and click **Home**.
3. Intercept the request, find the parameter:
   ```
   GET /?page=home HTTP/1.1
   ```
4. Change it to:
   ```
   GET /?page=/etc/natas_webpass/natas8 HTTP/1.1
   ```
5. Click **Forward** — the page will render the contents of the password file directly.

### What I Learned
* **Local File Inclusion (LFI)**: When user input is passed to `include()` or `require()` without sanitization, an attacker can read arbitrary files from the server.
* **Never Trust User Input in File Paths**: Always whitelist allowed page values instead of passing raw input to file-loading functions.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q</code>
</details>
