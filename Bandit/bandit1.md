# Bandit Level 0 → Level 1

### Level Goal
> search for passwords stored in the readme file and login to user bandit1 

### Discovery & Logic
1. **Analysis**: After successfully logging into bandit0, I had to look for a file called readme to get the key.
2. **Problem**: must ensure that the readme file is actually in the home directory.
3. **Solution**: After successfully logging in, I used the `ls` command to ensure the readme file existed, then used the `cat readme` command to extract the password from the file

### Commands Used
```bash
# to find out if the file really exists
ls

# to find out the contents of the file
cat readme

# exit session 
ssh bandit1@bandit.labs.overthewire.org -p 2220
```

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If</code>
</details>
