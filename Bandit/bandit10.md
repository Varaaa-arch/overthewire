# Bandit Level 9 → Level 10

### Level Goal
> The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several = characters.

### Discovery & Logic
1. **Analysis**: After logging in as bandit9, I found the file data.txt. Opening it normally produced unreadable characters, indicating that the file contains binary data instead of plain text. The hint says the password exists inside one of the human-readable strings, and it appears after several = characters.
2. **Problem**: 
    * **Binary File**: Using cat outputs messy, unreadable symbols.
    * **Hidden Text**: The password is embedded among binary content.
    * **Pattern Requirement**: I needed to locate readable text that follows multiple = characters.
3. **Solution**: First, I extracted readable strings from the binary file using the strings command. Then I filtered the result using grep to search for lines containing =. `strings data.txt | grep "="`


### Commands Used
```bash
# Extract readable strings and filter lines containing "="
strings data.txt | grep "="

# Exit session and login to next level
ssh bandit10@bandit.labs.overthewire.org -p 2220
```

### What I Learned
* **Binary vs Text Files**: Not all files are readable using cat; some require extraction tools.
* **Using strings**: The strings command helps reveal readable text hidden inside binary files — commonly used in reverse engineering and forensics.
* **Pattern Searching**: Searching for symbols (=) can help locate structured data or encoded secrets inside files.


### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey</code>
</details>
