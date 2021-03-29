import pygame
import time
import math
pygame.init()
screen =pygame.display.set_mode((500,600))
GREY=(52, 180, 235)
WHITE= (255,255,255)
BLACK=(0,0,0)
RED=(173, 0, 38)
BLUE=(17, 104, 245)
running=True
font=pygame.font.SysFont('sans',50)
text_1=font.render('+',True,BLACK)
text_2=font.render('-',True,BLACK)
text_3=font.render('+',True,BLACK)
text_4=font.render('-',True,BLACK)
text_5=font.render('Start',True,BLACK)
text_6=font.render('Reset',True,BLACK)
text_7=font.render('StopTimer', True,RED)
total_secs=0
start=False
total=0
while running:
 screen.fill(GREY)
 mouse_x,mouse_y=pygame.mouse.get_pos()
 
 pygame.draw.rect(screen,WHITE,(100,50,50,50)) #box1
 pygame.draw.rect(screen,WHITE,(100,200,50,50)) #box2
 pygame.draw.rect(screen,WHITE,(200,50,50,50)) #box3
 pygame.draw.rect(screen,WHITE,(200,200,50,50)) #box4
 pygame.draw.rect(screen,WHITE,(300,50,150,50)) #box5
 pygame.draw.rect(screen,WHITE,(300,200,150,50)) #box6

 screen.blit(text_1,(100,50))
 screen.blit(text_2,(100,200))
 screen.blit(text_3,(200,50))
 screen.blit(text_4,(200,200))
 screen.blit(text_5,(300,50))
 screen.blit(text_6,(300,200))


 pygame.draw.rect(screen,BLACK,(50,520,400,70))
 pygame.draw.rect(screen,WHITE,(60,530,380,50))
 screen.blit(text_7,(145,525))

 pygame.draw.circle(screen,BLACK,(250,400),100)
 pygame.draw.circle(screen,WHITE,(250,400),95)
 pygame.draw.circle(screen,WHITE,(250,400),95)

 # pygame.draw.line(screen,BLACK,(250,400),(250,310))
 for event in pygame.event.get():
 	if event.type==pygame.QUIT:

 		running=False

 	if event.type==pygame.MOUSEBUTTONDOWN:
 		if event.button==1:
 			if (100<mouse_x<150) and (50<mouse_y<100):
 				print("press + min")
 				total_secs+=60
 			if (200<mouse_x<250) and (50<mouse_y<100):
 				print("press + second")
 				total_secs+=1
 			if (100<mouse_x<150) and (200<mouse_y<250):
 				print("press - min")
 				total_secs-=60
 			if (200<mouse_x<250) and (200<mouse_y<250):
 				print("press - second")
 				total_secs-=1
 			if (300<mouse_x<450) and (50<mouse_y<100):
 				start=True
 				print("press Start")
 			if (300<mouse_x<450) and (200<mouse_y<250):
 				total_secs=0
 				start=False

 				print("press Reset")
 if start:
 	if total_secs>0 :
 	 total_secs-=1
 	 time.sleep(1)
 	elif total_secs==0:
 		start=False

 mins=int(total_secs/60)
 secs=total_secs-mins*60
 print(secs)
 print(mins)
 time_now=str(mins)+ ":"+str(secs)
 text_time=font.render(time_now,True,BLACK)
 screen.blit(text_time,(120,120))

 x_sec = 250+90*math.sin(6*secs*math.pi/180)
 y_sec = 400-90*math.cos(6*secs*math.pi/180)
 pygame.draw.line(screen,RED,(250,400),(x_sec,y_sec))

 x_min = 250+40*math.sin(6*mins*math.pi/180)
 y_min = 400-40*math.cos(6*mins*math.pi/180)
 pygame.draw.line(screen,BLUE,(250,400),(x_min,y_min))

 # if total!=0:
 # 	pygame.draw.rect(screen,RED,(60,530,int(380*(total_secs/total)),30))


 pygame.display.flip()
pygame.quit()