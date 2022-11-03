def imageLoader(dir_name, value):
    value = float(value)
    value = int(value)

    if value in range(1, 15):
        return dir_name+"\\img_1.png"
    elif value in range(15, 29):
        return dir_name+"\\img_2.png"
    elif value in range(29, 43):
        return dir_name+"\\img_3.png"
    elif value in range(43, 56):
        return dir_name+"\\img_4.png"
    elif value in range(56, 69):
        return dir_name+"\\img_5.png"
    elif value in range(69, 83):
        return dir_name+"\\img_6.png"
    else:
        return dir_name+"\\img_7.png"