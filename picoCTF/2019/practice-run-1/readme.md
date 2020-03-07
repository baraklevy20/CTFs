# Challenge
You're going to need to know how to run programs if you're going to get out of here. Navigate to /problems/practice-run-1_0_62b61488e896645ebff9b6c97d0e775e on the shell server and run this program to receive a flag.

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