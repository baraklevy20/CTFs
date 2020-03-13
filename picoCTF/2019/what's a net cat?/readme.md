# Challenge
Using netcat (nc) is going to be pretty important. Can you connect to 2019shell1.picoctf.com at port 21865 to get the flag?

# Solution
That's a similar challenge to `dont-use-client-side`.

We'll go with the same approach, we'll replace each condition with an assignment. e.g.
`password.charAt(0)  == 'd' &&` becomes `flag[0] = 'd'`.


Flag: `picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_51e7fd}`
