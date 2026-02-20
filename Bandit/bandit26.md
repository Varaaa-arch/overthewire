# Bandit Level 25 → Level 26

### Level Goal
> Use the SSH key found in Bandit 25 to log into Bandit 26. The main challenge is that Bandit 26 uses a restricted shell script that displays a text file and immediately terminates the connection, preventing normal command execution.

### Discovery & Logic
1. **Analysis**: By checking /etc/passwd, we see that bandit26 has its shell set to /usr/bin/showtext. Inspecting that script reveals it runs exec more ~/text.txt followed by exit 0. This means as soon as the file text.txt is finished being displayed, the session ends
2. **Problem**: If the terminal window is large enough, more displays the entire file instantly and exits, logging the user out before any commands can be entered. We need to "trap" the execution inside the more interface to prevent the script from reaching the exit command.
3. **Solution**: By shrinking the terminal window height, we force the more command to pause (waiting for user input to scroll). While paused, we can use the v shortcut to open the current file in the default editor (Vim). From inside Vim, we can bypass the restricted shell by manually setting the shell variable to /bin/bash and spawning a new interactive shell session.

### Commands Used
```bash
# Download the key from the server
scp -P 2220 bandit25@bandit.labs.overthewire.org:bandit26.sshkey .

# Set correct permissions
chmod 700 bandit26.sshkey

ssh -i bandit26.sshkey bandit26@bandit.labs.overthewire.org -p 2220

#Press v to open Vim.
# Inside Vim, type the following commands:
:set shell=/bin/bash
:shell
```

### What I Learned
* Restricted Shell Bypassing: Learned that any interactive tool (like more, less, or vi) that allows shell escaping can be used to break out of restricted environments.
* Terminal Environment Manipulation: Discovered that software behavior (like pagination) can be influenced by hardware-like constraints such as terminal window dimensions.
* Vim Shell Configuration: Understood how to redefine the internal $SHELL variable within Vim to spawn a standard bash session instead of the restricted default.
* SUID Binaries: Reaffirmed the use of SUID wrappers (bandit27-do) to perform tasks with higher-level privileges once initial access is gained.


### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ</code>
</details>
