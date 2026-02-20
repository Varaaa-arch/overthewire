# Bandit Level 28 → Level 29

### Level Goal
> There is a git repository at ssh://bandit28-git@bandit.labs.overthewire.org/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

### Discovery & Logic
1. **Analysis**: After cloning the repository, the README.md file contains a placeholder for the password (password: xxxxxxxxxx). This is a common scenario where sensitive information was accidentally committed and then "fixed" by overwriting it in a later commit.
2. **Problem**: The information we need is no longer in the "current" version of the files. However, Git is a version control system that records every single change made since the repository was created.
3. **Solution**: We need to inspect the commit history. By using the git log command, we can see the "diffs" (differences) for every commit. One commit has the description ‘fix info leak’. This sounds promising, so we want to see what changes where made. 


### Commands Used
```bash
# Clone the repository (Local Machine):
git clone ssh://bandit28-git@bandit.labs.overthewire.org:2220/home/bandit28-git/repo
cd repo
cat README.md

# Find the password in the diff
git log -p
```

### What I Learned
* Git Persistence: Learned that Git stores the entire history of a project. Simply editing a file and committing it doesn't delete the old data from the database.
* Git Log Patches: Mastered git log -p to view the chronological changes of a file, which is an essential tool for forensic analysis of a codebase.
* Commit Diffs: Understood how to read "diff" output, where - represents removed lines and + represents added lines.
* Data Leaks: Realized that sensitive data committed to Git is "compromised" forever unless the entire history is rewritten (which is difficult and discouraged).

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7</code>
</details>
