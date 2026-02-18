# Bandit Level 7 → Level 8

### Level Goal
> The password for the next level is stored in the file data.txt next to the word millionth.

### Discovery & Logic
1. **Analysis**: After logging in as bandit7, I found a file named data.txt. The challenge states that the password is located next to the word "millionth", meaning I only need to search for a specific line containing that keyword instead of reading the entire file manually.
2. **Problem**: 
    * **Large File**: The data.txt file contains many lines, making manual searching inefficient.
    * **Precise Matching**: I needed a command that could quickly locate a specific word inside a file.
    * **Efficient Text Searching**: Opening the file with cat would produce too much output.
3. **Solution**: I used the grep command, which is designed to search text patterns inside files. `grep "millionth" data.txt` 


### Commands Used
```bash
# Search for the keyword inside the file
grep "millionth" data.txt

# Exit session and login to next level
ssh bandit8@bandit.labs.overthewire.org -p 2220
```

### What I Learned
* **Text Searching with grep**: grep allows fast searching of specific words or patterns inside large files.
* **Efficient File Analysis**: Instead of reading entire files, filtering output saves time and improves workflow.


### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc</code>
</details>
~