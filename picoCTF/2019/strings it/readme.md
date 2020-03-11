# Challenge
Can you find the flag in file without running it? You can also find the file in /problems/strings-it_4_e276260a1b64a734b4178a280d25b754 on the shell server.

# Solution
We can use `grep` to find the flag. Since this is a binary file, we need to use the `-a` flag.
Furthermore, since we don't want to read until the end of the line, but we want only the matching, we'd use the `-o` flag.
So in total, `grep -ao picoCTF{.*} strings` would give us the flag.

Flag: `picoCTF{5tRIng5_1T_c611cac7}`