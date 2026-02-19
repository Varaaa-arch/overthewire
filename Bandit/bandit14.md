# Bandit Level 13 → Level 14

### Level Goal
> The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you are given a private SSH key to log into the next level.

### Discovery & Logic
1. **Analysis**: After logging in as bandit13, I found a file named: `sshkey.private`. Unlike previous levels, this file is not a password, but an SSH private key. This means authentication must be done using key-based login instead of a passwor
2. **Problem**: 
    * Several issues appeared during login:
    * SSH refused to use the private key.
3. **Solution**: I copied the provided private key to my local machine using scp over port 2220. After attempting to log in with the key using the ssh -i option, the connection failed due to insecure file permissions. To resolve this, I changed the permission of the private key to 600 using chmod, ensuring that only the file owner could read and write it. Once the permissions were corrected, SSH accepted the key and allowed login as bandit14. After successfully accessing the account, I read the password for the next level from /etc/bandit_pass/bandit14.

### Commands Used
```bash
scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private .

chmod 600 sshkey.private

ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220

cat /etc/bandit_pass/bandit14
```

### What I Learned
* **SSH Key Authentication**: Servers can authenticate users using cryptographic keys instead of passwords.
* **File Permission Security**: Private keys must have restricted permissions (600) or SSH will reject them.
* **Secure File Transfer**: scp allows encrypted file transfer via SSH.
* **Real Infrastructure Practice**: This mirrors real-world server access used in cloud and DevOps environments.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS</code>
</details>
