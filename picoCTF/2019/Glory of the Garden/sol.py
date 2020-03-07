if __name__ == "__main__":
    img = str(open('garden.jpg', 'rb').read())
    flag_start_index = img.index('picoCTF')
    flag = img[flag_start_index:img.index('}', flag_start_index) + 1]
    print(flag)
