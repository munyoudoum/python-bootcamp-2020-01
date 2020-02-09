import pygame, random, sys
from pygame.locals import *
from random import randint


def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
		return True
	else:
		return False
  
#font
font = "Retro.ttf"
#when die
def die(screen, score, score2):
	oww = pygame.mixer.Sound("oww.wav") #oww when die
	oww.play()
	f=pygame.font.SysFont(font, 30)
	t=f.render('Total Score: '+str(score+score2), True, (223, 125, 255))
	screen.blit(t, (10, 270))
	pygame.display.update()
	pygame.time.wait(2000)
	sys.exit()

xs = [100, 100, 100, 100, 100]
ys = [100, 80, 60, 40, 20]
dirs = 0
score = 0

xs2 = [500, 500, 500, 500, 500]
ys2 = [100, 80, 60, 40, 20]
dirs2 = 0
score2 = 0

#start game
pygame.init()

s = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snakit')
#music
music = pygame.mixer.music.load("soundtrack.mp3")
pygame.mixer.music.play(-1)
#bomb
bombsize = 70
bombimage = pygame.image.load("bomb.png").convert_alpha()
bombimage = pygame.transform.scale(bombimage, (bombsize, bombsize))
bombpos = (random.randint(20, 560), random.randint(20, 560))
#apple
appleimage = pygame.image.load("apple.png").convert_alpha()
appleimage = pygame.transform.scale(appleimage, (20, 20))
applepos = (random.randint(0, 580), random.randint(0, 580))
#snake
snake = pygame.Surface((20, 20))
snake.fill((randint(0, 255), 22, 211))
#snake2
snake2 = pygame.Surface((19, 19))
snake2.fill((25, 22, 211))
#screen
s.blit(appleimage, (100, 100))
f = pygame.font.SysFont('Arial', 20)
clock = pygame.time.Clock()


def text_format(message, textFont, textSize, textColor):
	newFont=pygame.font.Font(textFont, textSize)
	newText=newFont.render(message, 0, textColor)
	return newText


# Main Menu
def main_menu():
	menu=True
	selected="start"
	while menu:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_UP:
					selected="start"
				elif event.key==pygame.K_DOWN:
					selected="quit"
				if event.key==pygame.K_RETURN:
					if selected=="start":
						return True
					if selected=="quit":
						pygame.quit()
						quit()

		# Main Menu UI
		s.fill((4, 25, 255))
		title=text_format("Snakit", font, 90, (255, 111, 125))
		if selected=="start":
			text_start=text_format("START", font, 75, (255, 255, 255))
		else:
			text_start = text_format("START", font, 75, (0, 0, 0))
		if selected=="quit":
			text_quit=text_format("QUIT", font, 75, (255, 255, 255))
		else:
			text_quit = text_format("QUIT", font, 75, (0, 0, 0))


		title_rect=title.get_rect()
		start_rect=text_start.get_rect()
		quit_rect=text_quit.get_rect()

		# Main Menu Text
		s.blit(title, (600/2 - (title_rect[2]/2), 80))
		s.blit(text_start, (600/2 - (start_rect[2]/2), 300))
		s.blit(text_quit, (600/2 - (quit_rect[2]/2), 360))
		pygame.display.update()
		clock.tick(30)

main_menu()
time_counter = 0 #for bomb
while True:
	time_counter += clock.tick(10)
	for e in pygame.event.get():
		if e.type == QUIT:
			sys.exit(0)
		elif e.type == KEYDOWN:
			if e.key == K_w and dirs != 0:dirs = 2
			elif e.key == K_s and dirs != 2:dirs = 0
			elif e.key == K_a and dirs != 1:dirs = 3
			elif e.key == K_d and dirs != 3:dirs = 1
			elif e.key == K_UP and dirs2 != 0:dirs2 = 2
			elif e.key == K_DOWN and dirs2 != 2:dirs2 = 0
			elif e.key == K_LEFT and dirs2 != 1:dirs2 = 3
			elif e.key == K_RIGHT and dirs2 != 3:dirs2 = 1
		else:
			print(e)
	i = len(xs)-1
	while i >= 2:
		if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
			die(s, score, score2)
		i-= 1
	i2 = len(xs2)-1
	while i2 >= 2:
		if collide(xs2[0], xs2[i], ys2[0], ys2[i], 20, 20, 20, 20):
			die(s, score, score2)
		i2-= 1
#if touch bomb
	if collide(xs[0], bombpos[0], ys[0], bombpos[1], 20, bombsize, 20, bombsize):
		die(s, score, score2)
	if collide(xs2[0], bombpos[0], ys2[0], bombpos[1], 20, bombsize, 20, bombsize):
		die(s, score, score2)

#if touch apple
	if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10):
		score+=1
		snake.fill((randint(10, 255), randint(10, 255), randint(10, 255)))
		xs.append(700)
		ys.append(700)
		applepos=(random.randint(0,588), random.randint(0,588))

	if collide(xs2[0], applepos[0], ys2[0], applepos[1], 20, 10, 20, 10):
		score2+=1
		snake2.fill((randint(10, 255), randint(10, 255), randint(10, 255)))
		xs2.append(700)
		ys2.append(700)
		applepos=(random.randint(0,588), random.randint(0,588))


	if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580: die(s, score, score2)
	if xs2[0] < 0 or xs2[0] > 580 or ys2[0] < 0 or ys2[0] > 580: die(s, score, score2)
	i = len(xs)-1
	while i >= 1:
		xs[i] = xs[i-1]
		ys[i] = ys[i-1]
		i -= 1

	i2 = len(xs2)-1
	while i2 >= 1:
		xs2[i2] = xs2[i2-1]
		ys2[i2] = ys2[i2-1]
		i2 -= 1

	if dirs==0: ys[0] += 20
	elif dirs==1: xs[0] += 20
	elif dirs==2: ys[0] -= 20
	elif dirs==3: xs[0] -= 20

	if dirs2==0: ys2[0] += 20
	elif dirs2==1: xs2[0] += 20
	elif dirs2==2: ys2[0] -= 20
	elif dirs2==3: xs2[0] -= 20

	s.fill((255, 255, 255))
#snake movement
	for i in range(0, len(xs)):
		s.blit(snake, (xs[i], ys[i]))

	for i in range(0, len(xs2)):
		s.blit(snake2, (xs2[i], ys2[i]))

	s.blit(bombimage, bombpos)
	s.blit(appleimage, applepos)

	scoretext=f.render("Player 1: "+str(score), True, (0, 0, 0))
	s.blit(scoretext, (20, 20))
	scoretext2=f.render("Player 2: "+str(score2), True, (0, 0, 0))
	s.blit(scoretext2, (500, 20))
#bomb changing position every 10s
	if time_counter > 10000:
		bombpos = (random.randint(20, 560), random.randint(20, 560))
		time_counter = 0
		bombsize += 50
		bombimage = pygame.transform.scale(bombimage, (bombsize, bombsize))
	pygame.display.update()
