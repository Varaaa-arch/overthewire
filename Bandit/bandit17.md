# Bandit Level 16 → Level 17

### Level Goal
> The goal is to submit the current level's password to a specific port on localhost in the range 31000 to 32000. We need to find the port that uses SSL and returns a private key instead of just echoing the password.

### Discovery & Logic
1. **Analysis**: After scanning with nmap, several ports were open. We need to identify which one provides the credentials for the next level.
2. **Problem**: Standard nc (netcat) does not support SSL/TLS by default, so connecting to an SSL port with it will fail or hang.
3. **Solution**: Use `ncat --ssl` (or openssl s_client) to establish an encrypted connection to the target port (31790). Once connected, submitting the current password will trigger the server to provide an RSA Private Key.

### Commands Used
```bash
# Scanning NMAP
nmap -sV localhost -p 31000-32000

# 1. Retrieve the current password
cat /etc/bandit_pass/bandit16

# 2. Connect to the identified SSL port using ncat
ncat --ssl localhost 31790 

# 3. Paste the password and the server returns the RSA Private Key. 
# Copy the key and exit the Bandit server.

# 4. On your local machine, save the key using a text editor
nvim key

# 5. Restrict file permissions (SSH will reject the key if it's too open)
chmod 400 key

# 6. Log into the next level using the private key
ssh -i key bandit17@bandit.labs.overthewire.org -p 2220
```

### What I Learned
* **SSL/TLS Handshaking**: Learned that ncat --ssl is a convenient way to interact with encrypted services from the command line.
* **Key-Based Authentication**: Realized that not every level provides a simple text password. Some use RSA Private Keys for authentication, which is more secure.
* **SSH Identity Management**: Learned how to use the -i flag in SSH to specify a private key file for logging in, and the importance of chmod 400 to secure that key

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>[-]</code>
</details>
