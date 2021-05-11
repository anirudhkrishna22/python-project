from pygame import *
import pygame
import random
import time

start=time.time()
curTime=start

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)


root=display.set_mode((1200,700))   # create a window of given width and height
run=True
pygame.font.init()  # initializes the font module
myfont = pygame.font.SysFont('Comic Sans MS', 30)
height,width=65,110     # height and width of image
image_list=[image.load("D:\\downloads\\game_images\\audi logo.jpg"),image.load("D:\\downloads\\game_images\\benz logo.jpg"),image.load("D:\\downloads\\game_images\\bmw logo.jpg"),image.load("D:\\downloads\\game_images\\Bugatti-logo.png"),image.load("D:\\downloads\\game_images\\ferrari logo.png"),image.load("D:\\downloads\\game_images\\hummer logo.jpg"),image.load("D:\\downloads\\game_images\\jaguar logo.jpg"),image.load("D:\\downloads\\game_images\\lambo logo.jpg"),image.load("D:\\downloads\\game_images\\porsche-logo.png"),image.load("D:\\downloads\\game_images\\Rolls-Royce-Logo.jpg")] #list of images
for i in range(len(image_list)):
    image_list[i] =  transform.scale(image_list[i],(width,height))  # resize the image to given width and height
image_dict = {'AUDI': [] ,'BENZ':[] , 'BMW': [], 'BUGATTI':[],'FERRARI':[],'HUMMER':[],'JAGUAR':[],'LAMBO':[],'PORCHE':[],'ROLLS ROYCE':[]}

pos_list=[[i,j] for i in range(0,1200,120) for j in range(100,700,75)]
random.shuffle(pos_list)    # shuffles the list

q_mark=image.load("D:\\downloads\\game_images\\Question-mark-red-3D-glossy.jpg")
q_mark=transform.scale(q_mark,(width,height))

temp1=int(len(pos_list)/len(image_list))    # 8
temp2=0
click = []  # co-ordinates of clicked tile
for i in image_dict:
    image_dict[i] = pos_list[temp2:temp1+temp2]
    temp2+=temp1



click2=[]   # to store unique values of click
result=[]   # correctly clicked tiles co-ordinates
score=0
moves=0
while run:

    if time.time()>=curTime+1 :
        curTime+=1

    textsurface = myfont.render('score : '+ str(score), False, (0, 0, 0))
    moveText = myfont.render('moves : ' + str(moves), False, (0, 0, 0))
    timeText=myfont.render('time : ' + str(curTime-start), False, (0, 0, 0))

    for events in pygame.event.get():   # register all events from the user into an event queue
        if events.type==pygame.QUIT:
            run=False
            break
        if events.type==MOUSEBUTTONUP:  # check whether we clicked mouse or not
            mouse_pos = pygame.mouse.get_pos()
        else:
            mouse_pos = [-1,-1]

    root.fill((0,0,0))
    draw.rect(root,(190,190,190),(0,0,1200,100))
    root.blit(textsurface, (50, 20))
    root.blit(moveText, (350, 20))
    root.blit(timeText, (650, 20))

    for i in range(0,1200,120):
        for j in range(100,700,75):
            if [i,j] not in click and [i,j] not in result:
                root.blit(q_mark, (i, j))

############
    cur=0
    for i in image_dict:
        for j in image_dict[i]:
            if 0 <= mouse_pos[0]-j[0] <=width and 0 <= mouse_pos[1]-j[1] <= height:

                root.blit(image_list[cur],(j[0],j[1]))
                click.append(j)

        cur+=1

    for i in click:
        if i not in click2:
            click2.append(i)

    if len(click2)<3:
        for i in click2:
            cur1 = 0
            for k in image_dict:
                if i in image_dict[k]:
                    root.blit(image_list[cur1],(i[0],i[1]))
                    break
                cur1+=1

    if len(click2)==2:
        var=0
        for k in image_dict:
            if click2[0] in image_dict[k] and click2[1] in image_dict[k]:
                correctClick = mixer.music
                correctClick.play()
                result.append(click2[0])
                result.append(click2[1])
                var=1
        if var==0:
            score-=1
        elif var==1:
            score += 10
        moves+=1
        click2=[]
        click=[]

    display.update()


