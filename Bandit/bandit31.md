# Bandit Level 30 → Level 31

### Level Goal
> Clone the Git repository for bandit30-git and find the password for the next level. The password is not in the current files, the history, or the branches. You must explore other Git metadata to find it.

### Discovery & Logic
1. **Analysis**: After cloning the repo, README.md is empty or contains no password. Checking git branch -a shows no extra branches, and git log shows no previous versions containing the secret.
2. **Problem**: In Git, information can also be stored in Tags. A tag is a reference to a specific commit, but it can also be an "annotated tag" that contains its own message or data.
3. **Solution**: We need to check the repository for tags using git tag. Once a tag is found, we can use git show [tag_name] to inspect the data associated with that specific marker.

### Commands Used
```bash
# Clone the repository (Local Machine):
git clone ssh://bandit30-git@bandit.labs.overthewire.org:2220/home/bandit30-git/repo
cd repo

# Check for tags
git tag
git show secret
```

### What I Learned
* Git Tags: Learned that tags are persistent pointers to specific commits, often used for versioning (e.g., v1.0), but they can also store hidden information.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy</code>
</details>
