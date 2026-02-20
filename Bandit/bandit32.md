# Bandit Level 31 → Level 32

### Level Goal
> The goal is to push a specific file to a remote repository. You are given the filename (key.txt), the exact content ('May I come in?'), and the target branch (master). Success is defined by the server's response after a successful git push.

### Discovery & Logic
1. **Analysis**: After cloning the repo, the README.md provides strict instructions. However, checking the hidden files with ls -a reveals a .gitignore file.
2. **Problem**: 
    * Gitignore Constraint: The .gitignore file contains *.txt, which prevents Git from tracking any .txt files by default. If you try a normal git add key.txt, Git will ignore it.
    * Commit Requirement: Git requires a commit message to save changes. An empty message aborts the process.
    * Branch Discrepancy: While many modern systems use main, this specific challenge uses the legacy master branch. Pushing to the wrong branch name results in a refspec error.
3. **Solution**: Create the file key.txt with the required string, use git add -f (force) to bypass the .gitignore rule, commit the change with a descriptive message using git commit -m, push specifically to origin master

### Commands Used
```bash
# Clone the repository (Local Machine):
git clone ssh://bandit31-git@bandit.labs.overthewire.org:2220/home/bandit31-git/repo
cd repo

# Create the file and bypass the ignore rule
echo 'May I come in?' > key.txt
git add -f key.txt

# Commit & Push
git commit -m "Key"
git push origin master
```

### What I Learned
* Forcing Git: Learned that .gitignore is a safety feature, not a hard restriction; the -f flag allows you to add files that are otherwise excluded.
* Branch Specificity: Reaffirmed that master and main are distinct references. You must always push to the branch name defined by the remote repository.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K</code>
</details>
