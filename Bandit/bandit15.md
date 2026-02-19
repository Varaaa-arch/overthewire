# Bandit Level 14 → Level 15

### Level Goal
> The password for the next level can be retrieved by submitting the password of the current level to a service running on localhost at port 30000.

### Discovery & Logic
1. **Analysis**: After logging in as bandit14, the current level password could be obtained from `/etc/bandit_pass/bandit14`. The level instructions indicated that a network service was running locally on port 30000, meaning the password must be sent to that service to receive the next level’s credentials.
2. **Problem**: The challenge required interacting directly with a TCP service rather than reading files locally. This meant I needed a tool capable of opening a raw network connection and manually sending input to the service.
3. **Solution**: I used the nc (netcat) command to connect to localhost on port 30000. Netcat acts as a simple TCP client, allowing manual communication with network services. After establishing the connection, I submitted the current level password as input. The service validated the password and responded with a confirmation message followed by the password for the next level.

### Commands Used
```bash
cat /etc/bandit_pass/bandit14

nc localhost 30000
```

### What I Learned
* **Netcat (nc) Basics**: Netcat can open raw TCP connections to communicate with services.
* **Client–Server Interaction**: Some systems require sending data to a running service instead of reading files directly.
* **Localhost Concept**: localhost refers to the same machine (127.0.0.1).
* **Port Communication**: Services listen on specific ports and respond based on received input.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo</code>
</details>
