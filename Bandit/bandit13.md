# Bandit Level 11 → Level 12

### Level Goal
> The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed.

### Discovery & Logic
1. **Analysis**: After logging in as bandit12, I found data.txt. Opening it showed hexadecimal data instead of readable text. This indicates the file is a hexdump, meaning it must first be converted back into its original binary format before extracting the password.
2. **Problem**: 
    * **Hexdump Format**: The file is not directly usable and must be reversed into binary.
    * **Multiple Compression Layers**: The resulting file is compressed several times using different formats (gzip, bzip2, tar).
    * **Unknown Order**: Each extraction reveals another format, requiring repeated file identification.
3. **Solution**: [Step by Step](stepBandit13.md)

### What I Learned
* **Hexdump Reversal**: xxd -r converts hexadecimal dumps back into binary files.
* **Compression Formats in Linux**

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn</code>
</details>
