# Challenge
Can you find the robots? https://2019shell1.picoctf.com/problem/21868/ (link) or http://2019shell1.picoctf.com:21868

# Solution
We go to https://2019shell1.picoctf.com/problem/21868/robots.txt and find:
```
User-agent: *
Disallow: /e0779.html
```
We then go to https://2019shell1.picoctf.com/problem/21868/e0779.html and find our flag.

Flag: `picoCTF{ca1cu1at1ng_Mach1n3s_e0779}`