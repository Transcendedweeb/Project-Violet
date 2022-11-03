import pygame, os, threading

violet_first_img = pygame.image.load("images\\violet\\body\\img_00.PNG")	
violet_array = [violet_first_img]

intro_first_img = pygame.image.load("images\\intro\\comp\\img_0.PNG")
intro_array = [intro_first_img]

def totalFiles(dirName):
    list = os.listdir(dirName)
    number_files = len(list)
    return number_files

def imgLeafLoader(dir_name, array):
    for imgNumber in range(totalFiles(dir_name+"intro\\comp")-1):
        intro_array.append(pygame.image.load(dir_name+"intro\\comp" + "\\img_" + str(imgNumber+1) + ".PNG"))

    for imgNumber in range(totalFiles(dir_name+"sakura\\leaf")-1):
        if imgNumber+1 >= 10:
            array.append(pygame.image.load(dir_name +"sakura\\leaf"+ "\\img_" + str(imgNumber+1) + ".PNG"))
        else:
            array.append(pygame.image.load(dir_name +"sakura\\leaf"+ "\\img_0" + str(imgNumber+1) + ".PNG"))
    
    for imgNumber in range(totalFiles(dir_name+"violet\\body")-1):
        if imgNumber+1 >= 10:
            violet_array.append(pygame.image.load(dir_name +"violet\\body"+ "\\img_" + str(imgNumber+1) + ".PNG"))
        else:
            violet_array.append(pygame.image.load(dir_name +"violet\\body"+ "\\img_0" + str(imgNumber+1) + ".PNG"))

def threadGif(b, c):
    a = threading.Thread(target=imgLeafLoader, args=(b, c))
    a.setDaemon(True)
    a.start()