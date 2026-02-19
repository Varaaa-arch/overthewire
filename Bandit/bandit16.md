# Bandit Level 15 → Level 16

### Level Goal
> The goal of this level is to submit the password of the current level to port 30001 on localhost using SSL/TLS encryption to retrieve the next password.

### Discovery & Logic
1. **Analysis**: Unlike previous levels that used raw connections (like nc), this level requires SSL/TLS encryption. If you use a standard netcat connection, the server won't respond correctly because it expects an encrypted handshake.
2. **Problem**: How to send text data through a secure, encrypted tunnel via the terminal?
3. **Solution**: Use the `openssl s_client` utility. This command acts similarly to telnet or netcat but performs an SSL/TLS negotiation before opening the data communication channel. The -connect flag is used to specify the target host and port.

### Commands Used
```bash
# Connecting to localhost on port 30001 using SSL
openssl s_client -connect localhost:30001

# After the certificate info appears and the connection is established, 
# paste the password for Bandit 15:
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```

### What I Learned
* **SSL/TLS Client**: Learned that openssl s_client is a powerful tool for debugging or interacting with services that use encryption (like HTTPS, SMTPS, or custom encrypted ports).
* **Encrypted Communication**: Understood the difference between sending data in cleartext versus ciphertext. Port 30001 is configured to only accept connections that have successfully passed an SSL handshake.
* **Command Persistence**: Learned that once the SSL connection is active, you can interact with the remote service just like a regular shell session.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx</code>
</details>
