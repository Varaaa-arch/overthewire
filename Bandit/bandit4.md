# Bandit Level 1 → Level 2

### Level Goal
> This time, our mission is to find the password in a hidden file in the `inhere` directory. Then, log in as bandit4 on port 2220.

### Discovery & Logic
1. **Analysis**: After logging in as Bandit 3, I had to find the password to advance to the next level. The password was stored in the Inhere directory.
2. **Problem**: The file is hidden so even if you use `ls` it won't be found.
3. **Solution**: There are many ways to complete this mission. First, you have to enter the directory using `cd`, then you can use `ls -la`, or you can also use `find` and `du -a`. Well.. you can also use `find` without having to enter the directory and can directly use `cat`.

### Commands Used
```bash
# go into the directory
cd inhere

# search for hidden files
find 
#or 
du -ah
#or 
ls -la

# get the key
cat <that file>

# exit session and login
ssh bandit4@bandit.labs.overthewire.org -p 2220
```

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ</code>
</details>
