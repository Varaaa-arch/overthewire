# Bandit Level 13 → Level 14

### Level Goal
> The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions.

### Discovery & Logic
1. **Analysis**: After logging in as bandit11, I opened data.txt and noticed the text looked readable but meaningless. The level description mentions that all letters are rotated by 13 positions, which indicates a ROT13 cipher.
2. **Problem**: 
    * **Encoded Text**: The content is not encrypted but transformed using character rotation.
    * **Manual Decoding Impossible**: Decoding each character manually would be inefficient.
    * **Need Text Transformation Tool**: A command is required to shift letters back automatically.
3. **Solution**: I used the tr command, which translates or replaces characters. `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`

### Commands Used
```bash
# Decode ROT13 text
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'

# Exit session and login to next level
ssh bandit12@bandit.labs.overthewire.org -p 2220
```

### What I Learned
* **Text Transformation with tr**: The tr command can substitute characters efficiently.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4</code>
</details>
