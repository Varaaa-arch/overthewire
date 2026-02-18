# Bandit Level 5 → Level 6

### Level Goal
> The password for the next level is stored somewhere under the inhere directory, and it is: human-readable, 1033 bytes in size, not executable

### Discovery & Logic
1. **Analysis**: After entering the inhere directory, I found many subfolders and files. Manually checking each file would be impossible. The level hints gave three key properties for the password file: human-readable, exactly 1033 bytes, and non-executable.
2. **Problem**: 
    * **Too Many Files**: There are numerous files spread across subdirectories, making manual inspection inefficient.
    * **File Filtering Needed**: I needed a way to programmatically filter files based on size and permissions to match the criteria.
3. **Solution**: I used the find command to search recursively and filter by type, size, and permissions. The command: `find . -type f -size 1033c ! -executable`

### Commands Used
```bash
# Go into the directory
cd inhere

# Find the readable, non-executable file of exact size 1033 bytes
find . -type f -size 1033c ! -executable

# Display the password
cat <file>

# Exit session and login to next level
ssh bandit6@bandit.labs.overthewire.org -p 2220

```

### What I Learned
* **Advanced File Searching**: Learned to use find for searching files recursively with complex conditions.
* **Filtering by Size and Permissions**: How to combine -size and ! -executable to locate specific files in Linux.
* **Efficiency in Enumeration**: Instead of checking files manually, leveraging command-line tools automates the process—an essential skill in penetration testing and CTFs.


### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>HWasnPhtq9AVKe0dmk45nxy20cvUa6EG</code>
</details>
