from pwn import *
import os
import sys
sys.path.append(os.path.abspath("../../.."))
import credentials

sh = ssh(host='2019shell1.picoctf.com',
         user=credentials.username, password=credentials.password).run('sh')
sh.sendline(
    'cd /problems/first-grep--part-ii_2_1c866f894e7ef69b77a69a224b0c3f60/files')
sh.sendline('grep "picoCTF" -r .')
# sh.sendline('./vuln ' + 'a' * 133)
sh.interactive();
sh.close()
