# Bandit Level 6 → Level 7

### Level Goal
> The password for the next level is stored somewhere on the server and has all of the following properties: owned by user bandit7, owned by group bandit6, 33 bytes in size

### Discovery & Logic
1. **Analysis**: After logging in as bandit6, I needed to find a file that is owned by bandit7, belongs to group bandit6, and has a specific size of 33 bytes. Manually checking files across the system would take forever.
2. **Problem**: 
    * **File Ownership**: I needed a way to filter files by user and group ownership.
    * **File Size**: Exact size filtering required understanding how to specify units in the find command.
    * **Permission Errors**: When searching the whole system, some directories would throw Permission denied, cluttering output and slowing down the search.
3. **Solution**: I used find with combined conditions for user, group, and size: `find / -user bandit7 -group bandit6 -size 33c`


### Commands Used
```bash
# Search for the password file anywhere on the server
find / -user bandit7 -group bandit6 -size 33c 

# Display the password
cat <file>

# Exit session and login to next level
ssh bandit7@bandit.labs.overthewire.org -p 2220


```

### What I Learned
* **Filtering by Ownership**: Using -user and -group in find to locate files by their owner and group.
* **File Size Units in find**: c → bytes, k → kilobytes, M → megabytes, G → gigabytes
* **Efficient Enumeration**: Combining multiple conditions in find can drastically speed up file discovery, a crucial skill in CTFs and real-world penetration testing.


### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj</code>
</details>
