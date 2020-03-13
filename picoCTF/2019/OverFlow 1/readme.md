# Challenge
You beat the first overflow challenge. Now overflow the buffer and change the return address to the flag function in this program? You can find it in /problems/overflow-1_5_c76a107db1438c97f349f6b2d98fd6f8 on the shell server. Source.

# Solution
When a function gets called, its arguments, the `eip` register, the `ebp` register and the local variables are pushed to the stack.
If we write more than `64` (`FLAGSIZE`) to the buffer, these bytes will overflow to `eip` (and `ebp`). Thus we can control the return address. If we change the return address to the memory address of the `flag` function, we'll get the flag.

To get the memory address of `flag`, we'll use `radare2`. By using `r2 vuln` and then `is | grep flag` we can get the memory address of `flag` (`0x080485e6`).

So by using the following input, we'll get the flag:
```
input = [65] * 76 # 65 is some random value
input[76:] = [0xe6, 0x85, 0x04, 0x08, ord('\n')]
```


Flag: `picoCTF{n0w_w3r3_ChaNg1ng_r3tURn532066483}`
