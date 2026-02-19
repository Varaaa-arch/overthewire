# Bandit Level 17 → Level 18

### Level Goal
> There are two files in the home directory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between the two files.

### Discovery & Logic
1. **Analysis**: We need to find a specific difference between two large files. The standard tool for this in Linux is diff.
2. **Problem**: Upon logging in as bandit17, the connection is immediately closed by the server. This prevents an interactive shell session.
3. **Solution**: Use Remote Command Execution via SSH. By appending a command in quotes at the end of the ssh login string, the command is executed on the server and the output is sent back to our local terminal before the connection closes.

### Commands Used
```bash
# 1. List files to confirm they exist in the home directory
ssh -i key bandit17@bandit.labs.overthewire.org -p 2220 "ls"

# 2. Compare the two files to find the changed line
ssh -i key bandit17@bandit.labs.overthewire.org -p 2220 "diff passwords.old passwords.new"

# Output:
# 42c42
# < pGozC8kOHLkBMOaL0ICPvLV1IjQ5F1VA
# ---
# > x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
```

### What I Learned
* **SSH Remote Execution**: Learned that SSH can be used to run commands directly on a remote server without needing to maintain an interactive shell.
* **Diff Utility**: Understood how to read diff output. The < symbol indicates the line in the first file (old), while the > symbol indicates the line in the second file (new).
* **Bypassing Login Restrictions**: Learned that even if a .bashrc or profile script kicks you out, you can often still interact with the server by sending commands directly.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO</code>
</details>
