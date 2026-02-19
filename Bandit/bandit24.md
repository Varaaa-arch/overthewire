# Bandit Level 23 → Level 24

### Level Goal
> A program is running periodically at regular intervals as a cronjob. Check /etc/cron.d/ for the configuration and find out how the script works to retrieve the next password.

### Discovery & Logic
1. **Analysis**: Similar to the previous level, we start by looking at the cron jobs in /etc/cron.d/. We find cronjob_bandit23.
2. **Problem**: The script /usr/bin/cronjob_bandit23.sh uses dynamic variables. It doesn't use a fixed filename; instead, it calculates a target filename based on the output of a command:
`mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)`
3. **Solution**: The script is executed by user bandit23, meaning $myname inside the cronjob will be bandit23, to find where the password is hidden, we need to replicate that specific echo and MD5 command manually in our terminal, replacing $myname with bandit23. Once we get the MD5 hash (the filename), we can cat that file in the /tmp/ directory.

### Commands Used
```bash
# 1. Identify the cronjob for the next level
ls -la /etc/cron.d

# 2. View the cronjob configuration
cat /etc/cron.d/cronjob_bandit23

# 3. Analyze the script logic
cat /usr/bin/cronjob_bandit23.sh
# Logic: It takes "I am user bandit23", hashes it with MD5, and uses that as a filename in /tmp/

# 4. Replicate the script's logic to find the target filename
echo I am user bandit23 | md5sum | cut -d ' ' -f 1
# Output: 8ca319486bfbbc3663ea0fbe81326349

# 5. Read the generated file from the /tmp directory
cat /tmp/8ca319486bfbbc3663ea0fbe81326349
```

### What I Learned
* Variable Expansion: Learned how shell scripts use variables like $(whoami) to change behavior based on the user running the script.
* Hashing (MD5): Understood that MD5 can be used to create a unique "fingerprint" or identifier for a string.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>0Zf11ioIjMVN551jX3CmStKLYqjk54Ga</code>
</details>
