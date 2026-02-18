### Step 1 - /tmp
Since Bandit home directories are restricted, I created a writable workspace:
```bash
mkdir /tmp/vara
cp data.txt /tmp/vara
cd /tmp/vara
```

### Step 2 - Reverse the hexdump
Convert hex back into binary
```bash
xxd -r data.txt > data
```

### Step 3 - Identify File Type
Always check file type before extracting: `file data`. This revealed multiple compression formats sequentially.

### Step 4 - Repeated Extraction Process
I repeatedly followed this workflow: ***Check → Rename → Extract***

#### Gzip extraction
```bash
mv data data.gz
gzip -d data.gz
```
#### bzip2 extraction
```bash
mv data data.gz
gzip -d data.gz
```
#### tar extraction
```bash
mv data data.tar
tar -xf data.tar
```

### Step 5 - Final File
Eventually:
```bash
file data8
# Output : ASCII text

cat data8
```

### All Command Use
```bash
mkdir /tmp/vara
cp data.txt /tmp/vara
cd /tmp/vara

xxd -r data.txt > data
file data

mv data data.gz
gzip -d data.gz

mv data data.bz
bzip2 -d data.bz

mv data data.tar
tar -xf data.tar

# repeat identification + extraction
file <file>
mv <file> <correct_extension>
<decompression_command>

cat data8
ssh bandit13@bandit.labs.overthewire.org -p 2220

```