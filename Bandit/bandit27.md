# Bandit Level 26 → Level 27

### Level Goal
> The password for the next level is stored in /etc/bandit_pass/bandit27 and can only be read by user bandit27. In the home directory, there is a SUID binary that runs commands as another user. Use it to retrieve the password.

### Discovery & Logic
1. **Analysis**: Upon gaining a shell as bandit26 (after escaping the restricted more shell), we check the home directory and find an executable named bandit27-do. Checking its permissions with ls -la shows it has the SUID (Set User ID) bit set (indicated by the s in -rwsr-x---). This means when executed, it runs with the privileges of its owner, which is bandit27.
2. **Problem**: We cannot read /etc/bandit_pass/bandit27 directly as user bandit26 because we lack the necessary read permissions. We need a way to execute the cat command with bandit27's privileges.
3. **Solution**: The bandit27-do binary is a wrapper designed to execute any command provided as an argument with the permissions of user bandit27. By passing cat /etc/bandit_pass/bandit27 as an argument to this binary, we can bypass our current user restrictions and read the password file.

### Commands Used
```bash
bandit26@bandit:~$ ls -la
# Output: -rwsr-x--- 1 bandit27 bandit26 14876 Oct 14 09:26 bandit27-do

bandit26@bandit:~$ ./bandit27-do
# Output: Run a command as another user. Example: ./bandit27-do id

bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
# Output: upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB

```

### What I Learned
* Privilege Escalation via Wrappers: Learned how binary "wrappers" (like bandit27-do) function as a bridge to execute commands under a different user context.
* Argument Passing: Mastered the concept of passing system commands as arguments to SUID binaries to retrieve protected data.


### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB</code>
</details>
