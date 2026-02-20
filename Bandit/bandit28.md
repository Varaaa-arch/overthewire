# Bandit Level 27 → Level 28

### Level Goal
> The goal is to clone a Git repository located at ssh://bandit27-git@bandit.labs.overthewire.org/home/bandit27-git/repo on port 2220. The password for bandit27-git is the same as the one found in the previous level (bandit27). The password for the next level is stored inside this repository.

### Discovery & Logic
1. **Analysis**: This level shifts from standard file system navigation to Version Control Systems (VCS). Specifically, we need to interact with a remote Git repository. To do this, we need a local copy of the project.
2. **Problem**: Attempting to mkdir or git clone in restricted directories (like the root or someone else's home) results in a Permission denied error. Additionally, because the SSH server is running on a non-standard port (2220), we must format the Git URL correctly so it doesn't try to connect via the default port 22.
3. **Solution**: Navigate to a writable directory (like /tmp on the server or ~/Documents on a local machine). Use git clone with the specific port-inclusive URL format. Once the repository is cloned, inspect the files (usually a README or a text file) to find the password.

### Commands Used
```bash
# Create a directory on your laptop and enter it:
mkdir bandit_git
cd bandit_git

# Clone the repository (Local Terminal):
git clone ssh://bandit27-git@bandit.labs.overthewire.org:2220/home/bandit27-git/repo

# Navigate into the new folder and read the content
cd repo
ls
cat README
```

### What I Learned
* Linux Permissions: Confirmed that mkdir will fail if the parent directory does not have write permissions for the current user.
* Temporary Workspaces: Learned that /tmp is the standard location for performing temporary operations on shared Linux systems.


### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN</code>
</details>
