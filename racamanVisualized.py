import pygame
import sys
import random
import time
import math
pygame.init()
size = (1650,500)
background_color = pygame.Color(15,15,24)
arc_color_top = pygame.Color(173, 94, 132)
arc_color_bottom = pygame.Color(98, 252, 183)
window = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Racaman Visualized | Justin Stitt")

count = 1
index = 0
biggest = 0
numbers = [False] * 100000000
arcs = []
numbers[index] = True
screen_size = 500

class Arc():
    def __init__(self,start,end,dir):
        self.start = start
        self.end = end
        self.dir = dir
        self.diameter = abs(self.end - self.start) * 2
        self.x = (self.start + self.end) / 2

    def render(self):
        global screen_size


        #pygame.draw.rect(window,pygame.Color(0,255,0),pygame.Rect(screen_size,0,5,1000))
        print("The screen size is: {} and the biggest X value is: {}".format(screen_size,biggest))





        if self.dir == 0:
            pygame.draw.arc(window,arc_color_top,pygame.Rect(self.x,size[1]/2 - self.diameter/2,self.diameter,self.diameter),math.pi,0)

        else:
            pygame.draw.arc(window,arc_color_bottom,pygame.Rect(self.x,size[1]/2 - self.diameter/2,self.diameter,self.diameter),0,math.pi)






def step():
    global index,count,numbers,arcs,biggest
    next = index - count

    if (next < 0 or numbers[next] == True):
        next = index + count
    numbers[next] = True

    arc = Arc(index,next,count % 2)
    arcs.append(arc)
    index = next

    if index > biggest:
        biggest = index
    count += 1

def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    step()

def render():
    global screen_size
    for arc in arcs:
        arc.render()
    if biggest > screen_size:
        for arc in arcs:
            arc.diameter *= .5
            arc.diameter += 2
            arc.x -= 250
        screen_size += 500





while True:
    window.fill(background_color)
    update()
    render()
    pygame.display.flip()
    clock.tick(15)
