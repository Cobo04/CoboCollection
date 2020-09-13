import pygame
import os
import sys

# Window Initialization

pygame.init()
getScreenSize = pygame.display.Info()
screen = pygame.display.set_mode((getScreenSize.current_w - 200, getScreenSize.current_h - 200))
background = pygame.image.load(r'images\new_background.jpg')
pygame.display.set_caption('CoboClient: Cybersecurity Edition!')
gameIcon = pygame.image.load(r'images\coboclient_icon.png')
pygame.display.set_icon(gameIcon)
screen.fill((30, 30, 30))

# Color Initialization

color_white = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
button_color_active = pygame.Color('dodgerblue2')
button_color_inactive = pygame.Color('lightskyblue3')

# Font initialization

smallfont = pygame.font.SysFont("Corbel", 35)
myfont = pygame.font.SysFont('Comic Sans MS', 30)
pygame.font.init()
FONT = pygame.font.Font(None, 32)
# print(pygame.font.get_fonts())

# Variable Drivers

mouse_down = False
GUI_Editor = False
Allow_Edits = False
program_running = True
width = screen.get_width()
height = screen.get_height()
clock = pygame.time.Clock()
_ = True

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Classes

class InputBox():

    def __init__(self, X, Y, width, height, text = ''):
        self.rect = pygame.Rect(X, Y, width, height)
        self.color = button_color_inactive
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = button_color_active if self.active else button_color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.text != '':
                        # Do stuff with text
                        print(self.text)
                    self.text = ''
                    screen.fill((30, 30, 30))
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
    
    def resize(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def display(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

class buttonSystem():

    def GUI(self):
        global GUI_Editor
        global Allow_Edits 
        text = smallfont.render('GUI', True, color_white)
        if width - 108 <= mouse[0] <= width - 108+100 and height / 2 -430 <= mouse[1] <= 63: 
            pygame.draw.rect(screen,color_light,[width - 108, height / 2 -430, 100, 50])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GUI_Editor == False:
                    GUI_Editor = True
                    print('GUI Editor Enabled')
                    Allow_Edits = True
                else:
                    GUI_Editor = False
                    print('GUI Editor Disabled')
                    Allow_Edits = False
        else:
            pygame.draw.rect(screen,color_dark,[width - 108, height / 2 -430, 100, 50])
        screen.blit(text, (width - 87,height / 2 -420))

    def button1(self):
        text = smallfont.render('quit', True, color_white)
        if 100 <= mouse[0] <= 100+200 and 30 <= mouse[1] <= 70: 
            pygame.draw.rect(screen,color_light,[100,30,200,40])
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('bruh')
        else:
            pygame.draw.rect(screen,color_dark,[100,30,200,40])
        # screen.blit(text, (170,30))

    def button2(self):
        rect_box = pygame.draw.rect(screen,color_dark,[600,600,200,40])
        mouse = pygame.mouse.get_pos()
        global mouse_down
        if Allow_Edits == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
            if mouse_down == True:
                mousepositionx = mouse[0]
                mousepositiony = mouse[1]
                rect_box.move(800, 800)

    def get_mouse_position(self):
        mouse = pygame.mouse.get_pos()
        return(mouse)

    def display_mouse_position(self):
        mouse = pygame.mouse.get_pos()
        print('PosX: ' + str(mouse[0]) + ', PosY: ' + str(mouse[1]))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Functions

def get_events():
    # <!> Deprecated due to lag <!>
    global program_running
    # Key presses

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

def display_images():
    # <!> Deprecated due to lag <!>
    # Button System

        mouse = pygame.mouse.get_pos()
        # print('PosX: ' + str(mouse[0]) + ', PosY: ' + str(mouse[1]))
        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
            pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('Clicked on das booton')
        else:
            pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Application Loop

while program_running == True:

    # Input Box Augmentation
    input_box1 = InputBox(100, 100, 140, 32)
    input_boxes = [input_box1]
    finished = False

    while not finished:

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Button System

            buttonSystem.button1(1)
            buttonSystem.GUI(1)
            buttonSystem.button2(1)

            #Back to text box

            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
                    box.resize()
    
        for box in input_boxes:
            box.display(screen)
            
        pygame.display.flip()
        clock.tick(30)