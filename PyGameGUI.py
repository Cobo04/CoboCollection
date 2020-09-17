import pygame
import os
import sys

# Window Initialization

pygame.init()
SCALE = 1
getScreenSize = pygame.display.Info()
WIDTH = (getScreenSize.current_w - 200) * SCALE
HEIGHT = (getScreenSize.current_h - 200) * SCALE
Screen = pygame.display.set_mode((getScreenSize.current_w - 200, getScreenSize.current_h - 200))
background = pygame.image.load(r'images\new_background.jpg')
pygame.display.set_caption('CoboClient: Cybersecurity Edition!')
gameIcon = pygame.image.load(r'images\coboclient_icon.png')
pygame.display.set_icon(gameIcon)
clock = pygame.time.Clock()
Screen.fill((30, 30, 30))

# Font initialization

smallfont = pygame.font.SysFont("Corbel", 35)
myfont = pygame.font.SysFont('Comic Sans MS', 30)
pygame.font.init()
FONT = pygame.font.Font(None, 32)

# Colors

color_white = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
valueBoxOutline = (68, 68, 68)
button_color_active = pygame.Color('dodgerblue2')
button_color_inactive = pygame.Color('lightskyblue3')

# Scene appension and button setup

currentScene = [] # Scene that is currently being shown
scenes = [] #list of all the scenes
buttons = []
mouseDown = False
xOffset = 0
yOffset = 0
prevXOffset = 0
prevYOffset = 0


# Variables lol

Allow_GUI_Edits = False

class InputBox():

    def __init__(self, X, Y, width, height, text = ''):
        self.rect = pygame.Rect(X, Y, width, height)
        self.color = button_color_inactive
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global Allow_GUI_Edits
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
                        if self.text.lower() == 'enable gui editor':
                            if Allow_GUI_Edits == True:
                                print('GUI editor already enabled!')
                            else:
                                Allow_GUI_Edits = True
                                print('GUI Editor Enabled')
                        if self.text.lower() == 'disable gui editor':
                            if Allow_GUI_Edits == False:
                                print('GUI editor already disabled!')
                            else:
                                Allow_GUI_Edits = False
                                print('GUI editor disabled')
                        if self.text.lower() == 'quit':
                            print('Window terminated!')
                            pygame.quit()
                            sys.exit()
                            quit()
                        # print(self.text)
                    self.text = ''
                    Screen.fill((30, 30, 30))
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    Screen.fill((30, 30, 30))
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
    
    def resize(self):
        # Resize the box if the text is too long.
        width = max(690, self.txt_surface.get_width()+10)
        self.rect.w = width

    def display(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

input_box1 = InputBox(10, 12, 140, 32)
input_boxes = [input_box1]

class Scene:

    def __init__(self, objectList):
        global scenes
        #objectList takes a list of isntances of a class
        self.objects = objectList
        scenes.append(self)

    def display(self):
        pygame.event.pump()
        for button in self.objects:
            button.draw()
            button.check()

class Button:

    def __init__(self, x, y, width, height, text='', base_color=(0, 0, 0), hover_color = (255, 255, 255), text_offset = 0, function=None, Scene='default'):
        global buttons
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.base_color = base_color
        self.function = function
        self.rect = (self.x, self.y, self.width, self.height)
        self.hover_color = hover_color
        self.color = base_color
        self.text_offset = text_offset
        buttons.append(self)

    def checkIfClicked(self):
        if ((self.function == None) == False):
            exec(open(self.function).read())

    def draw(self):
        self.rect = (self.x, self.y, self.width, self.height)
        # Screen.blit(smallfont.render(self.text, True, color_white), (self.x + self.text_offset, self.y + self.text_offset))
        pygame.draw.rect(Screen, self.base_color, self.rect)

    def move(self, xOffset, yOffset):
        self.x += xOffset
        self.y += yOffset

    def check(self, event=None):
        global mouseDown
        global xOffset
        global yOffset
        global prevYOffset
        global prevXOffset
        
        mouse = pygame.mouse.get_pos()
        
        if ((mouse[0] > self.x) and (mouse[0] < self.x + self.width) and (mouse[1] > self.y) and (mouse[1] < self.y + self.height)):
            self.base_color = self.hover_color
            try:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDown = True
                    xOffset = self.x - mouse[0]
                    yOffset = self.y - mouse[1]
            except AttributeError:
                pass

            if mouseDown == True:
                if Allow_GUI_Edits == True:
                    self.x = mouse[0] + xOffset
                    self.y = mouse[1] + yOffset
 
        try:
            if event.type == pygame.MOUSEBUTTONUP:
                mouseDown = False
                xOffset = 0 * SCALE
                yOffset = 0 * SCALE
        except AttributeError:
            pass
        else:
            self.base_color = self.color

class valueBox:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        newBox = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(Screen, self.color, newBox, 2)

def checkEvents():
    global mouseDown
    global Allow_GUI_Edits

    for event in pygame.event.get():

        if event.type == pygame.QUIT :       
            pygame.quit()
            sys.exit()
            quit()

        if Allow_GUI_Edits == True:
            Screen.fill((30, 30, 30))

        #Draw Value Boxes

        for vB in vBList:
            valueBox.draw(vB)

        #Draw Buttons

        for button in currentScene[0].objects:
            button.check(event)
            button.draw()

        # Draw Input Boxes

        for box in input_boxes:
            box.handle_event(event)

    for box in input_boxes:
            box.resize()

    for box in input_boxes:
        box.display(Screen)

    pygame.display.update()

# Button appension (New button through button class)

button1 = Button(0, 300, 200, 50, 'hey', color_dark, color_light)
button2 = Button(0, 500, 200, 50, 'e', color_dark, color_light)
buttonsD = []
buttonsD.append(button1)
buttonsD.append(button2)
default = Scene(buttonsD)
currentScene.append(default)

# ValueBox appension

box1 = valueBox(WIDTH - 1010, HEIGHT - 868, 1000, 400, valueBoxOutline)
vBList = [box1]

# Slider appension

# PopUp appension

# BE ABLE TO CLICK ONLY WHEN GUI EDITOR IS ENABLED!!!
 
while True:

    checkEvents()
    currentScene[0].display()
