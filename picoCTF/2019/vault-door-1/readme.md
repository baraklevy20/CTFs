# Challenge
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: VaultDoor1.java

# Solution
That's a similar challenge to `dont-use-client-side`.

We'll go with the same approach, we'll replace each condition with an assignment. e.g.
`password.charAt(0)  == 'd' &&` becomes `flag[0] = 'd'`.


Flag: `picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_51e7fd}`