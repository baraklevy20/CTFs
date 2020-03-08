# Challenge
This should be easy. Overflow the correct buffer in this program and get a flag. Its also found in /problems/overflow-0_1_54d12127b2833f7eab9758b43e88d3b7 on the shell server. Source.

# Solution
The instructions says to overflow the correct buffer. We can see that if SIGSEGV is thrown, the flag is printed.
We can see that in line 18 we have an unsafe read into `buf`. If we overflow that buffer, eventually we'll overwrite `eip` and cause a SIGSEGV. When `vuln` is called, first `input` is pushed into the stack, then `eip`, then `ebp` and then the local variable `buf`.
If we write 133 bytes, it would write 128 of them to `buf`, then 4 to `ebp` and then one byte to `eip`. This would change the value of `eip`, casuing a SIGSEGV, and the flag would be printed.

Flag: `picoCTF{3asY_P3a5yb197d4e2}`