# Bandit Level 18 → Level 19

### Level Goal
> The password for the next level is stored in a file called readme in the home directory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

### Discovery & Logic
1. **Analysis**: When trying to log in normally, the server greets us with "Byebye!" and closes the connection. This is caused by a modified configuration file (like .bashrc) that executes an exit command upon login.
2. **Problem**: We need to read a file on the server, but we cannot maintain an interactive terminal session.
3. **Solution**: Use SSH to execute a specific command directly without requesting an interactive shell. By appending "cat readme" to the SSH command, the server executes only that command and returns the output before the login script can kick us out.

### Commands Used
```bash
# 1. Attempt to list files to see if the connection holds
ssh bandit18@bandit.labs.overthewire.org -p 2220 "ls"

# 2. After confirming 'readme' exists, read its content
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
```

### What I Learned
* **Shell Configuration Files**: Understood that files like .bashrc can be used to control user behavior, even to the point of forcing a logout.
* **Non-Interactive SSH**: Learned that SSH can be used as a transport layer for individual commands, which is a powerful way to bypass restrictive login environments.
* **Bypassing Forced Logout**: Discovered that "Remote Command Execution" is a key technique when a server's interactive shell is compromised or restricted.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8</code>
</details>
