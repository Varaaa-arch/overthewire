# Bandit Level 28 → Level 29

### Level Goal
> Clone the Git repository for bandit29-git and find the password for the next level. In this level, the password is not in the main branch's history, requiring you to explore other branches in the repository.

### Discovery & Logic
1. **Analysis**: Upon cloning the repository and checking README.md on the master branch, the password field says <no passwords in production!>. Checking git log on master also reveals nothing useful.
2. **Problem**: In professional software development, sensitive data or features under development are often kept off the master (production) branch. The password exists in the repository's database but is not currently visible in the "active" branch.
3. **Solution**: We need to check for other branches. By using git branch -a, we can see all local and remote branches. Once a development branch (like dev) is identified, we use git checkout to switch the working directory to that branch's version of the files.

### Commands Used
```bash
# Clone the repository (Local Machine):
git clone ssh://bandit29-git@bandit.labs.overthewire.org:2220/home/bandit29-git/repo
cd repo
cat README.md

# List all avaible branch
git branch -a
git checkout dev

cat README.md
```

### What I Learned
* Git Branching: Learned that a single Git repository can hold multiple "parallel universes" of code called branches.
* Tracking Remote Branches: Understood that git branch -a is necessary to see branches that exist on the server (origin) but haven't been downloaded to your local workspace yet.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL</code>
</details>
