# Challenge
This program executes any shellcode that you give it. Can you spawn a shell and use that to read the flag.txt? You can find the program in /problems/handy-shellcode_1_ebc60746fee43ae25c405fc75a234ef5 on the shell server. Source.

# Solution
We first start an interactive SSH session:
```
sh = ssh(host='2019shell1.picoctf.com', user='***', password='***').run('sh')
sh.sendline('cd /problems/handy-shellcode_1_ebc60746fee43ae25c405fc75a234ef5')
sh.interactive()
```
We then type `ls` and get `flag.txt  vuln    vuln.c`. If we try to read `flag.txt` we'll get a permission denied error, since only the owner has read permissions on that file.

We now look into `vuln`. The program takes as input shell script and executes it. So if we send it the assembly of a very basic interactive shell, the program would run a new interactive shell, this time with the owner permissions (as `vuln` is the one executing it).

 We therefore send it a basic shell executable by using `asm(shellcraft.sh())` as an input (using pwntools). This would run the new interactive shell. We can now execute `cat flag.txt` and get the flag.

Flag: `picoCTF{h4ndY_d4ndY_sh311c0d3_2cb0ff39}`