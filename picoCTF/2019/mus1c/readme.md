# Challenge
I wrote you a song. Put it in the picoCTF{} flag format

# Solution
At first I had no idea how to solve the challenge, so I used the hint. The hint says `Do you think you can master rockstar?` so I googled 'master rockstar' and found out it's a programming language, and those lyrics are actually code in the `rockstar` language.

By using a rockstar interpreter we get the following output:
```
114
114
114
111
99
107
110
114
110
48
49
49
51
114
```
Which translates to `rrrocknrn0113r` in ascii.

Flag: `picoCTF{rrrocknrn0113r}`
