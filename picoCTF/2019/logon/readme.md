# Challenge
The factory is hiding things from all of its users. Can you login as logon and find what they've been looking at? https://2019shell1.picoctf.com/problem/12284/ (link) or http://2019shell1.picoctf.com:12284

# Solution
After attempting to login, we find that an `admin` cookie is being set to `false`. By setting it to `true` and refreshing, we get the flag.

Flag: `picoCTF{th3_c0nsp1r4cy_l1v3s_6f2c20e9}`