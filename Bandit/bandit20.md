# Bandit Level 19 → Level 20

### Level Goal
> The goal is to use a setuid binary in the home directory to gain access to the password for the next level. This binary allows you to run commands with the privileges of another user.

### Discovery & Logic
1. **Analysis**: Checking the home directory reveals a file named bandit20-do. Looking at the permissions (-rwsr-x---), the s (setuid bit) indicates that this program runs as the owner (bandit20) rather than the current user (bandit19).
2. **Problem**: The password for Level 20 is stored in /etc/bandit_pass/bandit20, which is restricted. Only user bandit20 has the permission to read it.
3. **Solution**: Leverage the bandit20-do binary to execute the cat command. Since the binary runs with bandit20 privileges, it can bypass the file system restrictions on the password file.

### Commands Used
```bash
# 1. List files to identify the setuid binary and its owner
ls -la

# 2. Run the binary without arguments to understand its usage
./bandit20-do

# 3. List the password directory to confirm the target file exists
./bandit20-do ls /etc/bandit_pass

# 4. Execute the 'cat' command via the setuid binary to retrieve the password
./bandit20-do cat /etc/bandit_pass/bandit20
```

### What I Learned
* Setuid Bit (Special Permissions): Learned that the s bit in a file's permission string allows users to run that file with the owner's authority. This is common for utilities like passwd or sudo.
* Privilege Escalation Fundamentals: Understood how a single misconfigured or specifically designed setuid binary can be used to access data that is otherwise restricted.
* Wrapper Execution: Realized that binaries can act as "wrappers" to pass commands to the system shell under a different user context.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO</code>
</details>
