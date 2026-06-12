# Natas Level 6

> 🎥 **Video Walkthrough**: [Watch](/Natas/natas06.mp4)

### Level Goal
> The goal of this level is to find the password for the next level.

### Discovery & Logic
1. **Analysis**: The page shows a form asking for a **secret** input, and a link to view the source code.
2. **Problem**: The source code reveals the secret is loaded from an included file: `includes/secret.inc`. This file is publicly accessible.
3. **Solution**: Directly navigate to `http://natas6.natas.labs.overthewire.org/includes/secret.inc` to read the secret, then submit it in the form.

### Steps with Burp Suite

1. Open Burp Suite and make sure **Intercept is OFF** (we just need the browser to navigate freely).
2. Go to `http://natas6.natas.labs.overthewire.org/` and click **View sourcecode**.
3. Notice the PHP source includes:
   ```php
   include "includes/secret.inc";
   ```
4. In Burp's **Proxy** → **HTTP history**, find or manually send a GET request to:
   ```
   GET /includes/secret.inc HTTP/1.1
   Host: natas6.natas.labs.overthewire.org
   ```
5. The response will contain:
   ```php
   <?
   $secret = "FOEIUWGHFEEUHOFUOIU";
   ?>
   ```
6. Submit `FOEIUWGHFEEUHOFUOIU` in the form → password for natas7 is revealed.

### What I Learned
* **Information Disclosure via Include Files**: PHP `include` files (`.inc`) are often misconfigured to be web-accessible. They should be stored outside the webroot or protected with proper server rules.
* **Source Code Review**: Always check the source code link — developers sometimes expose sensitive logic or file paths directly in the frontend.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>bmg8SvU1LizuWjx3y7xkNERkHxGre0GS</code>
</details>
