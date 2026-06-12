# Natas Level 6

> 🎥 **Video Walkthrough**: [Watch on YouTube](https://youtu.be/UDuPYk83nzM?si=VKaC95YbdbjEIdvG)

### Level Goal
> The goal of this level is to find the password for the next level.

### Discovery & Logic
1. **Analysis**: The page shows a form asking for a **secret** input, and a link to view the source code.
2. **Problem**: The source code reveals the secret is loaded from an included file: `includes/secret.inc`. This file is publicly accessible.
3. **Solution**: Directly navigate to `http://natas6.natas.labs.overthewire.org/includes/secret.inc` to read the secret, then submit it in the form.

### Steps

1. Go to `http://natas6.natas.labs.overthewire.org/` and click **View sourcecode**.
2. Notice the PHP source includes:
   ```php
   include "includes/secret.inc";
   ```
3. Navigate directly to `http://natas6.natas.labs.overthewire.org/includes/secret.inc` in the browser.
4. The response will contain:
   ```php
   <?
   $secret = "FOEIUWGHFEEUHOFUOIU";
   ?>
   ```
5. Submit `FOEIUWGHFEEUHOFUOIU` in the form → password for natas7 is revealed.

### What I Learned
* **Information Disclosure via Include Files**: PHP `include` files (`.inc`) are often misconfigured to be web-accessible. They should be stored outside the webroot or protected with proper server rules.
* **Source Code Review**: Always check the source code link — developers sometimes expose sensitive logic or file paths directly in the frontend.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>bmg8SvU1LizuWjx3y7xkNERkHxGre0GS</code>
</details>
