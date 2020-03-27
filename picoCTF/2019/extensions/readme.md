# Challenge
This is a really weird text file TXT? Can you find the flag?

# Solution
When we open the text file we see it contains a lot of binary data, so it's probably not a text file.
We can see that it starts with "PNG" and has more PNG related strings such as "IHDR" or "RGB", so it's probably a PNG file. We change its extension from `txt` to `png`, and it's a valid image with our flag in it.

Flag: `picoCTF{now_you_know_about_extensions}`