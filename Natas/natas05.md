# Natas Level 5

> 🎥 **Video Walkthrough**: [Watch on YouTube](/Natas/natas05.mp4)

### Level Goal
> The goal of this level is to find the password for the next level.

### Discovery & Logic
1. **Analysis**: The page says *"Access disallowed. You are not logged in"*.
2. **Problem**: The server checks a **cookie** named `loggedin` to determine if the user is authenticated. By default, the cookie is set to `loggedin=0`.
3. **Solution**: Intercept the request with **Burp Suite** and change the cookie value from `0` to `1`.

### Steps with Burp Suite

1. Open Burp Suite, make sure **Intercept is ON** (`Proxy` → `Intercept` → `Intercept is on`).
2. Navigate to `http://natas5.natas.labs.overthewire.org/` in your browser (with Burp proxy configured).
3. The request will be captured in Burp. Look for the `Cookie` header:
   ```
   Cookie: loggedin=0
   ```
4. Change it to:
   ```
   Cookie: loggedin=1
   ```
5. Click **Forward** to send the modified request.
6. The page will now show the password for natas6.

### What I Learned
* **Cookie Manipulation**: Cookies are stored client-side and can be freely modified using tools like Burp Suite. Never use a cookie value alone as an authentication check without server-side validation.
* **Burp Suite Intercept**: Burp Suite's Proxy intercept lets you pause, read, and edit HTTP requests before they reach the server — essential for web security testing.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>0RoJwHdSKWFTYR5WuiAewauSuNaBXned</code>
</details>
