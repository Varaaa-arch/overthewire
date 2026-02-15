# Bandit Level 0 

### Level Goal
> The goal of this level is for you to log into the game using SSH

### Discovery & Logic
1. **Analysis**: asked to log in to the server using `SSH` with the username bandit0.
2. **Problem**: must know how to connect to the server using port 2220.
3. **Solution**: using the command `ssh -p [port]`.

### Commands Used
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

### What I Learned
* **SSH Basics**: Understand how to remotely log in to a server using the ssh command with a specific port specified using the -p flag.
* **Username Specification**: Learn that SSH defaults to the local OS username, so it must be explicitly defined (user@host) to avoid permission denied errors.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>bandit0</code>
</details>
