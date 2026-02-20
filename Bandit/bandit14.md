# Bandit Level 13 → Level 14

### Level Goal
> The goal is to retrieve the password from /etc/bandit_pass/bandit14. We are given a private SSH key (sshkey.private) in the home directory of Bandit 13 to log into Bandit 14.

### Discovery & Logic
1. **Analysis**: User bandit13 has a private SSH key (sshkey.private) in the home directory. This key belongs to user bandit14.
2. **Problem**: We need to access /etc/bandit_pass/bandit14, but we only have the key on the remote server. We want to move this key to our local machine to manage the connection from there.
3. **Solution**: scp to download the private key to the local terminal, adjust the file permissions to meet SSH security standards (700), and use it to log in as bandit14.

### Commands Used
```bash
scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private .   
chmod 700 sshkey.private
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
```

### What I Learned
* SCP File Transfer: Mastered how to securely download files from a remote server to a local machine using the SSH protocol.
* Private Key Security: Learned that SSH clients enforce strict security; a private key must have restricted permissions (like 600) or it will be ignored for being "too open."
* Identity Injection: Understood how to use the -i flag to bypass password prompts by injecting a digital identity file (Private Key) for authentication.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS</code>
</details>
