import pygame
import random 

pygame.init()
width = 1200
height = 700
white = (255,255,255)
grey = (192, 192, 192)
black = (0,0,0)
red = (200, 0, 0)

win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Hang Man By@oussama')

font = pygame.font.SysFont('comicsans', 64) 
text = font.render('Country Name', True, black, grey) 

words = []
text_file = open("word.txt","r")
for i in range(20):
	l = text_file.readline().replace('\n','')
	words.append(l)
word = random.choice(words)
print(word)
l = len(word)
ft = pygame.font.SysFont('comicsans', 32) 
txt = ft.render('_ '*l, True, black) 

class button():
	def __init__(self, color, x, y, width, height, text=''):
		self.color = color #color of the button
		self.x = x # x position of the button
		self.y = y # y position of the button 
		self.width = width # width position of the button
		self.height = height # height postion of the button
		self.text = text  # display text of the button

	def draw(self, win, outline=None):
		# to draw the border
		if outline:
			pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4),0)
		#to draw the button
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height),0)
		# to display button's text
		if self.text != '':
			font = pygame.font.SysFont('comicsans', 60)
			text = font.render(self.text, 1, (0,0,0))
			win.blit(text, (self.x + (round(self.width/2) - round(text.get_width()/2)), self.y + (int(self.height/2) - int(text.get_height()/2))))
	def isOver(self, pos):
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
		return False		

#create objects
b1 = button(grey, 40, 500, 40, 40 , 'A')
b2 = button(grey, 90, 500, 40, 40 , 'Z')
b3 = button(grey, 140, 500, 40, 40 , 'E')
b4 = button(grey, 190, 500, 40, 40 , 'R')
b5 = button(grey, 240, 500, 40, 40 , 'T') 
b6 = button(grey, 290, 500, 40, 40 , 'Y')
b7 = button(grey, 340, 500, 40, 40 , 'U')
b8 = button(grey, 390, 500, 40, 40 , 'I')
b9 = button(grey, 440, 500, 40, 40 , 'O')
b10 = button(grey, 490, 500, 40, 40 , 'P')
b11 = button(grey, 540, 500, 40, 40 , 'Q')
b12 = button(grey, 590, 500, 40, 40 , 'S')
b13 = button(grey, 640, 500, 40, 40 , 'D')
b14 = button(grey, 690, 500, 40, 40 , 'F')
b15 = button(grey, 740, 500, 40, 40 , 'G')
b16 = button(grey, 790, 500, 40, 40 , 'H')
b17 = button(grey, 840, 500, 40, 40 , 'J')
b18 = button(grey, 890, 500, 40, 40 , 'K')
b19 = button(grey, 940, 500, 40, 40 , 'L')
b20 = button(grey, 990, 500, 40, 40 , 'M')
b21 = button(grey, 390, 570, 40, 40 , 'W')
b22 = button(grey, 440, 570, 40, 40 , 'X')
b23 = button(grey, 490, 570, 40, 40 , 'C')
b24 = button(grey, 540, 570, 40, 40 , 'V')
b25 = button(grey, 590, 570, 40, 40 , 'B')
b26 = button(grey, 640, 570, 40, 40 , 'N')

lives = 7
font_heart = pygame.font.SysFont('comicsans', 16) 
txt_heart = font.render('<3: {}'.format(lives), True, red) 

def redrawWindow():
	win.fill(white)
	win.blit(text,(450,100))
	win.blit(txt, (500, 350))
	win.blit(txt_heart, (5,5))
	b1.draw(win, black)
	b2.draw(win, black)
	b3.draw(win, black)
	b4.draw(win, black)
	b5.draw(win, black)
	b6.draw(win, black)
	b7.draw(win, black)
	b8.draw(win, black)
	b9.draw(win, black)
	b10.draw(win, black)
	b11.draw(win, black)
	b12.draw(win, black)
	b13.draw(win, black)
	b14.draw(win, black)
	b15.draw(win, black)
	b16.draw(win, black)
	b17.draw(win, black)
	b18.draw(win, black)
	b19.draw(win, black)
	b20.draw(win, black)
	b21.draw(win, black)
	b22.draw(win, black)
	b23.draw(win, black)
	b24.draw(win, black)
	b25.draw(win, black)
	b26.draw(win, black)
	pygame.display.update()


while lives > 0:
	
	for event in pygame.event.get():
		pos = pygame.mouse.get_pos()

		if event.type == pygame.QUIT:
			pygame.quit()
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			if b1.isOver(pos):
				if b1.text in word:
					print('yes')
				else:
					lives -= 1
			elif b2.isOver(pos):
				if b2.text in word:
					print('yes')
				else:
					lives -= 1
			elif b3.isOver(pos):
				if b3.text in word:
					print('yes')
				else:
					lives -= 1
			elif b4.isOver(pos):
				if b4.text in word:
					print('yes')
				else:
					lives -= 1
			elif b5.isOver(pos):
				if b5.text in word:
					print('yes')
				else:
					lives -= 1
			elif b6.isOver(pos):
				if b6.text in word:
					print('yes')
				else:
					lives -= 1
			elif b7.isOver(pos):
				if b7.text in word:
					print('yes')
				else:
					lives -= 1
			elif b8.isOver(pos):
				if b8.text in word:
					print('yes')
				else:
					lives -= 1
			elif b9.isOver(pos):
				if b9.text in word:
					print('yes')
				else:
					lives -= 1
			elif b10.isOver(pos):
				if b10.text in word:
					print('yes')
				else:
					lives -= 1
			elif b11.isOver(pos):
				if b11.text in word:
					print('yes')
				else:
					lives -= 1
			elif b12.isOver(pos):
				if b12.text in word:
					print('yes')
				else:
					lives -= 1
			elif b13.isOver(pos):
				if b13.text in word:
					print('yes')
				else:
					lives -= 1
			elif b14.isOver(pos):
				if b14.text in word:
					print('yes')
				else:
					lives -= 1
			elif b15.isOver(pos):
				if b15.text in word:
					print('yes')
				else:
					lives -= 1
			elif b16.isOver(pos):
				if b16.text in word:
					print('yes')
				else:
					lives -= 1
			elif b17.isOver(pos):
				if b17.text in word:
					print('yes')
				else:
					lives -= 1
			elif b18.isOver(pos):
				if b18.text in word:
					print('yes')
				else:
					lives -= 1
			elif b19.isOver(pos):
				if b19.text in word:
					print('yes')
				else:
					lives -= 1
			elif b20.isOver(pos):
				if b20.text in word:
					print('yes')
				else:
					lives -= 1
			elif b21.isOver(pos):
				if b21.text in word:
					print('yes')
				else:
					lives -= 1
			elif b22.isOver(pos):
				if b22.text in word:
					print('yes')
				else:
					lives -= 1
			elif b23.isOver(pos):
				if b23.text in word:
					print('yes')
				else:
					lives -= 1
			elif b24.isOver(pos):
				if b24.text in word:
					print('yes')
				else:
					lives -= 1
			elif b25.isOver(pos):
				if b25.text in word:
					print('yes')
				else:
					lives -= 1
			elif b26.isOver(pos):
				if b26.text in word:
					print('yes')
				else:
					lives -= 1



	redrawWindow()