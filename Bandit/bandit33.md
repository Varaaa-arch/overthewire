# Bandit Level 32 → Level 33

### Level Goal
> After the Git challenges, you are faced with a restricted shell. The goal is to escape this custom shell and gain access to a standard shell to read the password for Level 33.

### Discovery & Logic
1. **Analysis**: Upon logging in, you are greeted by the "WELCOME TO THE UPPERCASE SHELL". Any command you type is automatically converted to uppercase before the system attempts to execute it.
2. **Problem**: The shell acts as a high-pass filter that breaks any letter-based command. To escape, we need a command that does not contain letters, or a way to call the underlying shell using a reference that the uppercase filter cannot ruin.
3. **Solution**: In Linux shell scripting, Positional Parameters are special variables. The variable $0 represents the name of the current script or the shell itself. 
Because $0 is a symbol and a number, the uppercase transformation has no effect on it. When you execute $0, you are telling the system: "Run the program that is currently running me." In this environment, that program is the standard /bin/sh or /bin/bash.

### Commands Used
```bash
# Login SSH
ssh bandit32@bandit.labs.overthewire.org -p 2220

>> whoami
sh: 1: WHOAMI: not found
>> ls
sh: 1: LS: not found

# Execute the escape command:
>> $0
cat /etc/bandit_pass/bandit33
```

### What I Learned
* Shell Variable $0: Learned that $0 is a powerful tool to reference the shell binary itself, often used in "jailbreaks" to spawn a sub-shell.
* Case Sensitivity: Deepened my understanding of how Linux handles command execution and how simple text filters can be bypassed using special characters.
* Restricted Environments: Understood that custom shells are often just "wrappers" around standard shells, and finding a way to call the parent process can lead to a full escape.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0</code>
</details>
