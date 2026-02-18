# Bandit Level 10 → Level 11

### Level Goal
> The password for the next level is stored in the file data.txt, which contains base64 encoded data.

### Discovery & Logic
1. **Analysis**: After logging in as bandit10, I found a file named data.txt. Opening it showed a long string of seemingly random characters consisting of letters, numbers, +, /, and = symbols. This pattern is typical of Base64 encoding.
2. **Problem**: 
    * **Encoded Data**: The content is not plain text but encoded.
    * **Unreadable Password**: The password cannot be used until the data is decoded.
    * **Correct Tool Needed**: I needed a Linux command capable of decoding Base64 data.
3. **Solution**: Linux provides a built-in command called base64 that can decode encoded content using the -d flag. `base64 -d data.txt`

### Commands Used
```bash
# Decode base64 encoded data
base64 -d data.txt

# Exit session and login to next level
ssh bandit11@bandit.labs.overthewire.org -p 2220
```

### What I Learned
* **Base64 Encoding**: Base64 is an encoding method used to represent binary data in ASCII format.
* **Decoding Data in Linux**: The base64 -d command converts encoded data back into readable text.
* **Encoding vs Encryption**: Base64 is not encryption, only encoding meaning it can easily be reversed.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr</code>
</details>
