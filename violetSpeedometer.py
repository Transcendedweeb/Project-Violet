def imageLoader(dir_name, value):
    value = float(value)
    value = int(value)
    range_nmbr1 = 0
    range_nmbr2 = 2

    for e in range(1,52):
        if (value >= range_nmbr1) and (value < range_nmbr2):
            return dir_name+"\\img_"+str(e)+".png"
        elif value > 99:
            return dir_name+"\\img_51.png"
        else:
            range_nmbr1 = range_nmbr1 + 2
            range_nmbr2 = range_nmbr2 + 2