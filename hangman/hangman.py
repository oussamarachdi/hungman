import pygame, os, math, sys
import random 
from pygame.locals import *

pygame.init()
pygame.mixer.init()


main_clock = pygame.time.Clock()
#colors

white = (255,255,255)
grey = (192, 192, 192)
black = (0,0,0)
red = (200, 0, 0)
green = (0, 200, 0 )

# display window
width = 1200
height = 700
win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Hang Man By@oussama')

#------------------------------------------------------------------------------------
#uploding images
images = []
for i in range(7):
	image = pygame.image.load('images/hangman'+ str(i) +'.png')
	images.append(image)

# loading guessing words
words = []
text_file = open("word.txt","r")
for i in range(20):
	l = text_file.readline().replace('\n','')
	words.append(l)
word = random.choice(words)
guessed = []
print(word)
#buttons variables
r = 25
g = 20
ls = []
sx = round((width - (g + r*2)*13) / 2)
sy = 500
A = 65 # ord('A')=65

for i in range(26): #26 buttons
	x = sx + g * 2 + ((r * 2 +g)*(i % 13))
	y = sy + ((i // 13) * (g + r * 2))
	ls.append([x, y, chr(A+i), True]) 

# Fonts 

font = pygame.font.SysFont('bahnschrift', 50) 
text = font.render(' Country Name ', True, black) 

l = len(word)
ft = pygame.font.SysFont('comicsans', 60)  

letter_font = pygame.font.SysFont('comicsans', 40)
def display_message(message, color):
	pygame.time.delay(1000)
	win.fill(color)
	text = ft.render(message,1,black)
	win.blit(text, (int(width/2 - text.get_width()/2), int(height/2 - text.get_height()/2)))
	pygame.display.update()
	pygame.time.delay(3000)


def redrawWindow():
	win.fill(white)
	win.blit(images[status], (900,100))
	win.blit(text,(int(width/2 - text.get_width()/2),90))
	# Draw Word
	display_word = ""
	for letter in word:
		if letter in guessed:
			display_word += letter + " "
		else:
			display_word += "_ "
	txt = ft.render(display_word, True, black)	
	win.blit(txt, (100, 300))	
	#draw letters

	for letter in ls:
		x, y, ltr, visible = letter
		if visible:
			pygame.draw.circle(win, black, (x, y), r, 3)
			t = letter_font.render(ltr, True, black)
			win.blit(t, (int(x - t.get_width()/2), int(y - t.get_height()/2)))
	pygame.display.update()
	
#Game Variables
status = 0

#Game LOOP
FPS = 60
clock = pygame.time.Clock()
run = True
while run:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()	
		if event.type == pygame.MOUSEBUTTONDOWN:
			mx, my = pygame.mouse.get_pos()
			for letter in ls:
				x, y, ltr, visible = letter
				if visible:
					dis = math.sqrt((x-mx)**2+(y-my)**2)
					if dis <= r:
						letter[3] = False
						guessed.append(ltr)
						print(guessed)
						if ltr not in word:
							pygame.mixer.music.load('music/incorrect.wav')
							pygame.mixer.music.play(0)
							status += 1
	won = True
	for letter in word:
		if letter not in guessed:
			won = False
			break
	if won:
		pygame.mixer.music.load('music/win.wav')
		pygame.mixer.music.play(0)
		display_message("You Won!!", green)
	if status == 6 :
		pygame.mixer.music.load('music/lost.wav')
		pygame.mixer.music.play(0)
		display_message("You Lost!!", red)

	redrawWindow()
pygame.quit()
