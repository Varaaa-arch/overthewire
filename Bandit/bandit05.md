# Bandit Level 4 → Level 5

### Level Goal
> Find the password in the inherent directory, where it is stored in the only human-readable file.

### Discovery & Logic
1. **Analysis**: After entering the inside folder, I found many files with names starting with a hyphen (like -file00, -file01, etc.). I had to check each one to see which ones contained plain text (ASCII text), because passwords couldn't possibly be stored in messy binary files.
2. **Problem**: 
    * **Number of Files**: There are quite a lot of files, and it's tiring to have to cat them one by one.
    * **Strange Character**: If I randomly cat binary files, the terminal can error out or display strange, unintelligible symbols.
    * **File Name**: The files start with a hyphen (-), so I need the ./ trick again like in the previous level.
3. **Solution**: I use the file command. This command is powerful because it can tell you the type of file without having to open it. I use wildcards (asterisk *) to check all files at once: file ./-*. After finding the type ASCII text, then I opened it using paint.

### Commands Used
```bash
# Check the type of all files in the folder
file ./inhere/*

# get the key
cat <that file>

# exit session and login
ssh bandit5@bandit.labs.overthewire.org -p 2220
```

### What I Learned
* **File Classification**: Menggunakan perintah file untuk mengidentifikasi tipe data di dalam suatu file (karena di Linux, ekstensi file tidak menentukan isinya).
* **Human-Readable Data**: Belajar cara memfilter atau mencari file yang berisi teks biasa (ASCII text) di tengah kumpulan file binary atau data yang tidak bisa dibaca manusia.


### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw</code>
</details>
