# Bandit Level 20 → Level 21

### Level Goal
> To gain access to the next level, you must connect to a service on localhost and send it the password of the current level. If the password is correct, the service will send back the password for the next level.

### Discovery & Logic
1. **Analysis**: There is a setuid binary called ./suconnect. It works by connecting to a port provided as an argument, sending the current level's password, and expecting the same password in return.
2. **Problem**: We need to "catch" the connection from ./suconnect. If we just run it, there is nothing listening on the other side.
3. **Solution**: Create a local listener using nc -l -p [port]. By piping our current password (echo -n '...' | nc) and running it in the background with &, we create a mini-server that waits for ./suconnect to connect. Once they "shake hands" and verify the password, the server sends us the next level's password.

### Commands Used
```bash
# 1. Start a Netcat listener on port 1234 in the background.
# This will wait for a connection and then send the Bandit 20 password.
echo -n '0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO' | nc -l -p 1234 &

# [1] 24  <-- This indicates the background process ID (PID)

# 2. Run the suconnect binary and tell it to connect to our background listener.
./suconnect 1234
```

### What I Learned
* Network Handshaking: Learned how two local processes can communicate through network sockets (localhost).
* Job Control (&): Understood how to push a command to the background, allowing the terminal to run a second command (the client) simultaneously.
* Netcat (nc) as a Server: Used Netcat's listening mode (-l) to act as a temporary server to facilitate data exchange.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>EeoULMCra2q0dSkYj561DX7s1CpBuOBt</code>
</details>
