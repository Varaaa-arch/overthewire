# Bandit Level 2 → Level 3

### Level Goal
> This mission is the same as level 2, you have to find the password in the file, but the difference is that this file has spaces `--spaces in this filenames--`. After finding it, you have to log in as bandit3 with port 2220.

### Discovery & Logic
1. **Analysis**: I'm logged in as bandit2. The password for the next level is in a file named `--spaces in this filename--`.
2. **Problem**: In the Linux terminal, spaces are used as separators between commands. If I type cat spaces in this filename, the cat command will look for a file named spaces, then a file named in, and so on. Because there are no files named in that way, the error "No such file or directory" appears.
3. **Solution**: In this mission, I use double quotes `" "` to wrap the file names into one. So that Linux will read it as 1 file.

### Commands Used
```bash
# to find out if the file really exists
ls

# to find out the contents of the file
cat "./--spaces in this filename--"

# exit session and login
ssh bandit3@bandit.labs.overthewire.org -p 2220
```

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx</code>
</details>
