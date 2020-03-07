from pwn import *

sh = ssh(host='2019shell1.picoctf.com',
         user='***', password='***').run('sh')
sh.sendline(
    'cd /problems/practice-run-1_0_62b61488e896645ebff9b6c97d0e775e')
sh.interactive()
