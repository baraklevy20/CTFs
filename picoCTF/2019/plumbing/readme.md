# Challenge
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to 2019shell1.picoctf.com 63345.

# Solution
When we run `nc 2019shell1.picoctf.com 63345` we can see we're getting too many lines. The terminal is set to only show 1000 lines (at least on vscode), which means we have to use pipes. We can either save the output to a file `nc 2019shell1.picoctf.com 63345 > log.txt` and search it, or we can use the `|` pipe to use another command on the output of the previous command. So `nc 2019shell1.picoctf.com 63345 | grep picoCTF` will give us our flag. 

Flag: `picoCTF{digital_plumb3r_4e7a5813}`
