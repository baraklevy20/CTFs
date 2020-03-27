# Challenge
Theres something in the building. Can you retrieve the flag?

# Solution
This time running `strings buildings.png` doesn't help much. We try some steganography tools. We decide to use zsteg which includes LSB checks and by running `zsteg buildings.png | grep picoCTF` we find our flag.

Flag: `picoCTF{h1d1ng_1n_th3_b1t5}`