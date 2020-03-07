# Challenge
The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help `UFJKXQZQUNB` with the key of `SOLVECRYPTO`. Can you use this table to solve it?.

# Solution
Basically in other words, the crypted letter 'U' was obtained by using the table with letter 'S'. So by going to row 'S' (or column 'S'),
and finding 'U', by looking at the column, we can see the original (decrypted) letter (in our case 'C').

In general, we take the current crypted character ('U'), subtract the current key character ('S'), get 2 which is the third letter (0 indexing). Thus we get 'C'. Since this is circular, we modulo by 26. We do this for all characters and get the flag.

Flag: `picoCTF{CRYPTOISFUN}`