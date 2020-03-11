import re

# checkpass.substring(0, split) == 'pico') -> flag[0:split] = pico
split = 4
conditions = """if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == 'e2f2') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_e') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == '4}') {""".splitlines()


flag = [None] * 32
for condition in conditions:
    m = re.search("checkpass.substring\((.*), (.*)\) == '(.*)'", condition)
    flag[eval(m.group(1)):eval(m.group(2))] = m.group(3)
print(''.join(flag))
