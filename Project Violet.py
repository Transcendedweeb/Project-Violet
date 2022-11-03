import pygame, sys, os, datetime
from pygame.locals import *
import pyautogui as keys
import pydirectinput

import violetGIF, violetMetrix, violetSpeedometer, violetBattery, violetVoiceCMD
import violetAi as AI

intro_counter = [False]
main_counter = [0]

# Sprite classes
class GifLeafs(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        first_img = pygame.image.load("images\\sakura\\leaf\\img_00.PNG")	
        self.sprites = [first_img]
        violetGIF.threadGif("images\\", self.sprites)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def update(self,speed):
        self.current_sprite += speed
        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

class GifViolet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.current_sprite = 0
        self.image = violetGIF.violet_array[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def update(self,speed):
        self.current_sprite += speed
        if int(self.current_sprite) >= len(violetGIF.violet_array):
            self.current_sprite = 0
        self.image = violetGIF.violet_array[int(self.current_sprite)]

class GifIntro(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.current_sprite = 0
        self.image = violetGIF.intro_array[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def update(self,speed):
        self.current_sprite += speed
        if int(self.current_sprite) >= len(violetGIF.intro_array):
            self.current_sprite = 0
            violetMetrix.pog_array[0] = "mainState"
        self.image = violetGIF.intro_array[int(self.current_sprite)]
# ___________________________________________

# Game-state class
class GameState():
    def mainState(self, cpu_counter, ram_counter):
        # exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # ___________________________________________

        # Backgound
        screen.blit(bg, (0,0))
        # ___________________________________________

        # Blit/Render text (CPU)
        if cpu_counter >= 1.0:
            text_cpu = font_13misa.render(violetMetrix.cpu_array[len(violetMetrix.cpu_array)-1], True, (255,255,255))
            cpu_counter = 0.0
            last_cpu_value = violetMetrix.cpu_array[len(violetMetrix.cpu_array)-1]

            som_image1 = pygame.image.load(violetSpeedometer.imageLoader("images\\speedometer", violetMetrix.cpu_array[len(violetMetrix.cpu_array)-1]))

            violetMetrix.cpu_array.clear()
            violetMetrix.cpu_array.append(last_cpu_value)
            #print(violetMetrix.cpu_array)
        else:
            cpu_counter = cpu_counter + 0.0006
        screen.blit(text_cpu, (305, 90))
        screen.blit(percentage_icon, (403, 90))
        screen.blit(under_cpu_text, (315, 130))
        screen.blit(som_image1, (250,5))
        # ___________________________________________

        # Blit/Render text (RAM)
        if ram_counter >= 1.0:
            text_ram = font_13misa.render(violetMetrix.ram_array[len(violetMetrix.ram_array)-1], True, (255,255,255))
            ram_counter = 0.0
            last_ram_value = violetMetrix.ram_array[len(violetMetrix.ram_array)-1]

            som_image2 = pygame.image.load(violetSpeedometer.imageLoader("images\\speedometer", violetMetrix.ram_array[len(violetMetrix.ram_array)-1]))

            violetMetrix.ram_array.clear()
            violetMetrix.ram_array.append(last_ram_value)
            #print(violetMetrix.ram_array)
        else:
            ram_counter = ram_counter + 0.0006
        screen.blit(text_ram, (550, 90))
        screen.blit(percentage_icon, (648, 90))
        screen.blit(under_ram_text, (560, 130))
        screen.blit(som_image2, (495,5))
        # ___________________________________________

        # Disk blit/render
        disk_text = font_13misa.render("Alpha Drive:", True, (255,255,255))
        disk_FS = font_13misa.render(violetMetrix.getDiskFS(), True, (255,255,255))
        disk_P = font_13misa.render(violetMetrix.getDiskP(), True, (255,255,255))
        diskP_float = float(violetMetrix.getDiskP()[0:3])
        bat_image = pygame.image.load(violetBattery.imageLoader("images\\battery", diskP_float))

        screen.blit(disk_text, (370, 250))
        screen.blit(disk_FS, (460, 300))
        screen.blit(disk_P, (460, 350))
        screen.blit(bat_image, (400,295))
        # ___________________________________________

        # light render
        if violetVoiceCMD.listner_list[0] == "green":
            screen.blit(green_light, (715, 392))
        else:
            screen.blit(red_light, (715, 392))
        # ___________________________________________

        # Run sprites
        violet_Group.draw(screen)
        violet_Group.update(0.2)

        leaf_Group.draw(screen)
        leaf_Group.update(0.2)
        # ___________________________________________

        pygame.display.update()

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        if intro_counter[0] == False:
            keys.keyDown("win")
            pydirectinput.keyDown("shift")
            pydirectinput.keyDown("right")

            keys.keyUp("win")
            pydirectinput.keyUp("shift")
            pydirectinput.keyUp("right")

            intro_counter[0] = True
            # print(intro_counter[0])

        if main_counter[0] >= 1:
            pygame.display.set_mode((800,480), FULLSCREEN)
            main_counter[0] = -1
            # print("test")
        elif main_counter[0] >= 0 and main_counter[0] < 1:
            main_counter[0] = 1
        

        intro_Group.draw(screen)
        intro_Group.update(0.1)

        pygame.display.update()

    def mssBoard(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                AI.violet_text_list[0] = ""
                violetMetrix.pog_array[0] = "mainState"

        screen.blit(bg_img2, (0, 0)) 
        # mss_text = font_stix.render(AI.violet_text_list[0], False, (255,255,255))

        sentences = [word.split('\n') for word in AI.violet_text_list[0].splitlines()]
        x = 420
        y = 85
        for line in sentences:
            mss_text = font_stix.render(str(line[0]), False, (0,0,0))
            screen.blit(mss_text, (x, y))
            y = y+38

        global delay_counter
        if delay_counter == True:
            delay_counter = False
            pygame.time.wait(8000)
            violetMetrix.pog_array[0] = "mainState"
        else:
            delay_counter = True
            pygame.display.update()


    def stateManager(self):
        cpu_counter = 2.0
        ram_counter = 2.0

        if violetMetrix.pog_array[0] == "mainState":
            self.mainState(cpu_counter, ram_counter)

        if violetMetrix.pog_array[0] == "intro":
            self.intro()

        if violetMetrix.pog_array[0] == "mssboard":
            self.mssBoard()
# ___________________________________________


# Main pygame setup
pygame.init()
screen = pygame.display.set_mode((800,480))
pygame.display.toggle_fullscreen
pygame.display.set_caption('Project Violet')
bg = pygame.image.load("background.png")
icon = pygame.image.load("images\\iconMain.png")
pygame.display.set_icon(icon)
violetMetrix.threadMatrix()
# ___________________________________________

# Font setup
pygame.font.init()
font_stix = pygame.font.Font('font\\STIXTwoText-Regular.ttf', 35)
font_13misa = pygame.font.Font('font\\13_Misa.ttf', 35)
# ___________________________________________

# Intro setup
intro_test = pygame.image.load("images\\intro\\800x480.png")
# ___________________________________________

# Metrix setup
percentage_icon = font_13misa.render("%", True, (255,255,255))
under_cpu_text = font_13misa.render("CPU", True, (255,255,255))
under_ram_text = font_13misa.render("RAM", True, (255,255,255))

    # Speedometer setup
som_image1 = pygame.image.load("images\\speedometer\\img_1.png")
som_image2 = pygame.image.load("images\\speedometer\\img_1.png")
# ___________________________________________

# Sprite setup
intro_Group = pygame.sprite.Group()
intro_Sprite = GifIntro(0,0)
intro_Group.add(intro_Sprite)

leaf_Group = pygame.sprite.Group()
leaf_Sprite = GifLeafs(10,10)
leaf_Group.add(leaf_Sprite)

violet_Group = pygame.sprite.Group()
violet_Sprite = GifViolet(-75,0)
violet_Group.add(violet_Sprite)
# ___________________________________________

# Background 2 setup
bg_img2 = pygame.image.load("images\\messageboard\\mb_v2.png")
delay_counter = False
# ___________________________________________

# light setup
green_light = pygame.image.load("images\\light\\green_light.png")
red_light = pygame.image.load("images\\light\\red_light.png")
# ___________________________________________

# Start new log
try:
    os.remove("AIconfig\\logs.txt")

    log_file = open("AIconfig\\logs.txt", "x")
    log_file.close()
except:
    log_file = open("AIconfig\\logs.txt", "w")
    moment_in_time = str(datetime.datetime.now().time())
    log_file.write("["+moment_in_time[0:7]+"] "+ "logs.txt was not found in directory, new file created.\n\n")
    log_file.close()
# ___________________________________________

print(violetVoiceCMD.threadVoice())

while True:
    game_state = GameState()
    # GameState.mainState(cpu_counter, ram_counter)
    game_state.stateManager()