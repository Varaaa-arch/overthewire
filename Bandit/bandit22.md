# Bandit Level 21 → Level 22

### Level Goal
> A program is running periodically at regular intervals as a cronjob. Look in /etc/cron.d/ for the configuration and see what command is being executed.

### Discovery & Logic
1. **Analysis**: In Linux, scheduled tasks are often managed by the cron daemon. The configuration files for these tasks are stored in /etc/cron.d/.
2. **Problem**: We need to find a script that runs as bandit22 and see if it exposes any credentials.
3. **Solution**: List the contents of /etc/cron.d/ to find relevant jobs, Read the cron configuration for bandit22 to find the path of the script being executed, Analyze the shell script (.sh) to see what it does, The script reveals that it copies the password for the next level into a world-readable file in /tmp/.

### Commands Used
```bash
# 1. List all cron jobs to find the one for the next level
ls -la /etc/cron.d

# 2. Read the cronjob configuration for bandit22
cat /etc/cron.d/cronjob_bandit22
# Output indicates it runs /usr/bin/cronjob_bandit22.sh every minute

# 3. Read the actual script to see its behavior
cat /usr/bin/cronjob_bandit22.sh

# Script Content:
# chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
# cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

# 4. Read the temporary file where the password was redirected
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

### What I Learned
* Cronjobs: Learned that cron is a time-based job scheduler in Unix-like operating systems. Files in /etc/cron.d/ define who runs what and how often.
* Script Analysis: Practiced reading basic bash scripts to understand data flow (in this case, redirecting a protected file to a public one).
* Insecure Temporary Files: Understood a common security flaw where sensitive data is moved to a publicly accessible location (/tmp/) with weak permissions.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q</code>
</details>
