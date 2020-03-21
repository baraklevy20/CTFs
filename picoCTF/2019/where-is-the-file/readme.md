# Challenge
I've used a super secret mind trick to hide this file. Maybe something lies in /problems/where-is-the-file_6_8eae99761e71a8a21d3b82ac6cf2a7d0.

# Solution
We connect to the shell server and run `ls`, and nothing shows up. The file is probably hidden, so we use `ls -a` to show hidden files. We then see `.  ..  .cant_see_me`. We use `cat .cant_see_me` to get the flag.

Flag: `picoCTF{w3ll_that_d1dnt_w0RK_a88d16e4}`