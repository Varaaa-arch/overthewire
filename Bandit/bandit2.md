# Bandit Level 1 → Level 2

### Level Goal
> Have to find the password for the next level, the password is stored in the file `-`. After knowing the password login as bandit2 with port 2220

### Discovery & Logic
1. **Analysis**: I've logged in as bandit1, and this time the mission is to find the password in the file -.
2. **Problem**: When I search for the file `-` using `ls` and see the contents of the file using `cat -`, nothing appears (blank) and I can't do anything with it.
3. **Solution**: Well, I found out that the `-` sign in Linux is standard input (stdin) and not a file name, so `cat` is confusing. We have to use `./-` to find out the password

### Commands Used
```bash
# to find out if the file really exists
ls

# to find out the contents of the file
cat ./-

# exit session and login
ssh bandit2@bandit.labs.overthewire.org -p 2220
```

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>263JGJPfgU6LtdEvgfWU1XP5yac29mFx</code>
</details>
