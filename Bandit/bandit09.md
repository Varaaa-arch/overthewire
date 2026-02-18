# Bandit Level 8 → Level 9

### Level Goal
> The password for the next level is stored in the file data.txt and is the only line of text that occurs only once.

### Discovery & Logic
1. **Analysis**: After logging in as bandit8, I found a file named data.txt containing many repeated lines. The challenge states that the password is the only unique line, meaning it appears exactly once in the file.
2. **Problem**: 
    * **Duplicate Lines**: Most lines appear multiple times, so visually inspecting the file would be inefficient.
    * **uniq Limitation**: The uniq command only works correctly if duplicate lines are adjacent, meaning the file must be sorted first.
    * **Data Filtering**: I needed a way to isolate lines that occur only once.
3. **Solution**: I combined sort and uniq commands using a pipe (|). `sort data.txt | uniq -u`


### Commands Used
```bash
# Sort the file and display only unique lines
sort data.txt | uniq -u

# Exit session and login to next level
ssh bandit9@bandit.labs.overthewire.org -p 2220
```

### What I Learned
* **Pipeline Usage (|)**: Learned how to chain commands together so one command’s output becomes another’s input.
* **Sorting Before uniq**: uniq only detects consecutive duplicates, so sorting is often required first.
* **Finding Unique Data**: Useful technique for log analysis, anomaly detection, and data filtering.
* **Common uniq Options**: uniq -u → show only unique lines, uniq -d → show duplicated lines, uniq -c → count occurrences


### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>4CKMh1JI91bUIZZPXDqGanal4xvAg0JM</code>
</details>
